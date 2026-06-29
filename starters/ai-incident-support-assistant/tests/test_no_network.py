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

NETWORK_MODULES = {
    "socket", "ssl", "urllib", "http", "ftplib", "smtplib", "telnetlib",
    "poplib", "imaplib", "nntplib", "xmlrpc", "requests", "httpx", "urllib3",
    "aiohttp", "websocket", "websockets", "pycurl",
}


def python_files():
    for dirpath, dirnames, filenames in os.walk(STARTER_ROOT):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        for name in filenames:
            if name.endswith(".py"):
                yield os.path.join(dirpath, name)


def imported_roots(path):
    with open(path, "r", encoding="utf-8") as handle:
        tree = ast.parse(handle.read(), filename=path)
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                roots.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                roots.add(node.module.split(".")[0])
    return roots


class TestNoNetwork(unittest.TestCase):
    def test_no_starter_script_imports_network(self):
        offenders = []
        files = list(python_files())
        self.assertTrue(files, "expected to find starter Python files")
        for path in files:
            bad = imported_roots(path) & NETWORK_MODULES
            if bad:
                rel = os.path.relpath(path, STARTER_ROOT)
                offenders.append(f"{rel} imports {sorted(bad)}")
        self.assertEqual(offenders, [], "network imports found: " + "; ".join(offenders))


if __name__ == "__main__":
    unittest.main(verbosity=2)
