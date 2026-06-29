#!/usr/bin/env python3
"""Guard: the starter scripts must not import any network module.

Standard library only. Static check — parses each Python file in the starter with
`ast` and asserts none import a networking module. This keeps the starter offline by
construction (no LLM, no API, no network), which is a core Level 1 guarantee.

Run with:  python3 tests/test_no_network.py
"""

import ast
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
STARTER_ROOT = os.path.normpath(os.path.join(HERE, os.pardir))

# Network modules: forbidden in ANY starter Python file.
NETWORK_MODULES = {
    "socket", "ssl", "urllib", "http", "ftplib", "smtplib", "telnetlib",
    "poplib", "imaplib", "nntplib", "xmlrpc", "requests", "httpx", "urllib3",
    "aiohttp", "websocket", "websockets", "pycurl",
}

# Escape hatches: forbidden in the runtime scripts (scripts/). Test files legitimately
# use importlib to load the module under test, so this stricter rule is scoped.
ESCAPE_MODULES = {"subprocess", "importlib", "ctypes", "multiprocessing"}
ESCAPE_CALL_ATTRS = {"system", "popen", "popen2", "popen3", "popen4", "import_module"}
ESCAPE_CALL_NAMES = {"__import__", "eval", "exec"}


def python_files():
    for dirpath, dirnames, filenames in os.walk(STARTER_ROOT):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for name in filenames:
            if name.endswith(".py"):
                yield os.path.join(dirpath, name)


def parse(path):
    with open(path, "r", encoding="utf-8") as handle:
        return ast.parse(handle.read(), filename=path)


def imported_roots(tree):
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                roots.add(node.module.split(".")[0])
    return roots


def escape_calls(tree):
    hits = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Attribute) and func.attr in ESCAPE_CALL_ATTRS:
                hits.add(func.attr)
            elif isinstance(func, ast.Name) and func.id in ESCAPE_CALL_NAMES:
                hits.add(func.id)
    return hits


def is_runtime_script(path):
    return os.sep + "scripts" + os.sep in path


class TestNoNetwork(unittest.TestCase):
    def test_no_starter_script_imports_network(self):
        offenders = []
        files = list(python_files())
        self.assertTrue(files, "expected to find starter Python files")
        for path in files:
            bad = imported_roots(parse(path)) & NETWORK_MODULES
            if bad:
                offenders.append(f"{os.path.relpath(path, STARTER_ROOT)} imports {sorted(bad)}")
        self.assertEqual(offenders, [], "network imports found: " + "; ".join(offenders))

    def test_runtime_scripts_have_no_escape_hatches(self):
        offenders = []
        for path in python_files():
            if not is_runtime_script(path):
                continue
            tree = parse(path)
            bad_imports = imported_roots(tree) & ESCAPE_MODULES
            bad_calls = escape_calls(tree)
            if bad_imports or bad_calls:
                rel = os.path.relpath(path, STARTER_ROOT)
                offenders.append(f"{rel}: imports={sorted(bad_imports)} calls={sorted(bad_calls)}")
        self.assertEqual(offenders, [], "escape hatches found: " + "; ".join(offenders))


if __name__ == "__main__":
    unittest.main(verbosity=2)
