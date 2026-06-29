# Formação Polaris em Applied AI Engineering
## Do fundamento crítico à construção de aplicações de IA avaliáveis, seguras e defensáveis
*Polaris Applied AI Engineering Formation*

---

> **Status — draft v0.1.**
> Documento canônico interno da Polaris. Define a **arquitetura da formação, padrões, níveis, rubricas e critérios** — **não** é o curso, nem material didático final.
> A validar por uma **primeira cohort** e por **alunos autodidatas** antes de virar v1.
> Princípio que rege todo o documento: **Self-paced first. Cohort optional. Mentor optional. Review optional.**

> **O que este documento é e o que não é.**
> Este é o **documento canônico** (a fonte única de arquitetura e padrões). Os **materiais didáticos reais** — *module pages, lab guides, troubleshooting guides, FAQs, reference solutions, templates, starter repos* — e as **cohorts opcionais** virão depois (Seção 18). Este documento não deve ser transformado em curso completo.

---

## Sumário

- [0. Comece aqui](#0-comece-aqui)
- [1. Visão executiva](#1-visão-executiva)
- [2. Tese central da formação](#2-tese-central-da-formação)
- [3. Relação com a Polaris Academy](#3-relação-com-a-polaris-academy)
- [4. Professional Core](#4-professional-core)
- [5. Self-Paced Learning Experience](#5-self-paced-learning-experience)
- [6. Projeto-mãe](#6-projeto-mãe)
- [7. Arquitetura geral da formação](#7-arquitetura-geral-da-formação)
- [8. Padrões obrigatórios da formação](#8-padrões-obrigatórios-da-formação)
- [9. Nível 1 — AI Foundations for Builders](#9-nível-1--ai-foundations-for-builders)
- [10. Nível 2 — AI Builder](#10-nível-2--ai-builder)
- [11. Nível 3 — AI Application Engineer](#11-nível-3--ai-application-engineer)
- [12. Applied AI Engineering Capstone](#12-applied-ai-engineering-capstone)
- [13. Rubricas](#13-rubricas)
- [14. Caminhos por perfil](#14-caminhos-por-perfil)
- [15. Materiais e curadoria](#15-materiais-e-curadoria)
- [16. Decision logs consolidados](#16-decision-logs-consolidados)
- [17. Backlog pós-v0.1](#17-backlog-pós-v01)
- [18. Auditoria crítica final](#18-auditoria-crítica-final)

---

## 0. Comece aqui

Entrada para autodidatas. Encontre sua linha, faça os próximos 30 minutos e publique a primeira evidência. Os comandos abaixo **nunca dependem de versões futuras do projeto** — começam pelo setup, não pela demo.

| Eu sou / quero… | Próximos 30 minutos | 1º arquivo | 1º comando | 1ª evidência | Principal risco |
|---|---|---|---|---|---|
| **Só usar IA melhor** | ler o track de literacia; montar 1 workflow de prompts | `ai-literacy/README.md` | — (sem código) | um workflow documentado (post/notion) | achar que está "construindo" |
| **Dev e quero construir** | rodar o Foundations Check; abrir o starter | `problem-framing.md` (template) | `make setup` → `make test` | repo público com setup verde + `progress.md` iniciado | tratar LLM como "só mais uma API" e pular evals |
| **Iniciante técnico** | instalar ambiente; primeiro commit | `README.md` do starter | `make setup` → `make check` | 1º repo com README + CI verde | tutorial hell; pular o baseline |
| **Data analyst / data scientist** | rodar Foundations Check; mapear o que pular | `problem-framing.md` | `make setup` → `make test` | `progress.md` + plano (pula ML clássico) | subestimar que a lacuna é engenharia, não ML |
| **Staff / principal** | revisar a arquitetura do projeto-mãe; escolher uma decisão para registrar | `docs/architecture.md` (leitura) | `make setup` | esboço de um ADR | pular a mão-na-massa e perder intuição de custo/falha |
| **Produto / negócio** | ler camadas + problem framing; escrever 1 trade-off memo | `problem-framing.md` (leitura) | — | trade-off memo "precisa de IA?" | liderar sem entender evals |
| **Quero fazer o Capstone** | revisar Níveis 1–3; abrir o MVP Capstone | `submission/capstone-summary.md` (template) | `make setup` → `make test` | `progress.md` + checklist do Core | demo do caminho feliz sem falhas/limites |

> Regra do primeiro passo: para quem está começando a construir, o primeiro comando é `make setup` / `make test` / `make check` ou abrir `problem-framing.md` — **não** `make demo` (que só faz sentido em versões posteriores do projeto).

---

## 1. Visão executiva

**O que é.** Uma formação **orientada a projeto e autodidata** que leva alguém com base de engenharia a **construir, avaliar e operar aplicações reais de IA** (LLM apps, RAG, tool calling) — com medição, custo, segurança e governança. Aprende-se construindo **um único sistema que cresce**: o *AI Incident & Support Assistant*.

**Para quem é.** Desenvolvedores (backend/frontend/fullstack/QA/DevOps) e pessoas com fundamentos de engenharia que querem entrar em Applied AI Engineering com critério; iniciantes motivados (via a ponte do Common Core); e — apenas no track curto de literacia — quem quer **usar** IA melhor.

**Para quem não é.** Quem quer apenas usar ChatGPT no dia a dia (faça só o track `AI Literacy & Productivity` e pare); quem quer ser **ML researcher** (a formação dá base e aponta a trilha, mas não é o foco).

**Promessa realista.** Ao final, você constrói e **defende** uma aplicação de IA medida e segura. Não é "especialista em 30 dias"; não forma pesquisador; não promete emprego.

**"Do zero ao especialista" sem inflar título.** "Specialist" aqui é **direção de maturidade**, não selo. Concluir a formação significa **prontidão (readiness)** para atuar como Applied AI Engineer e **caminhar** rumo a Specialist — que é julgamento acumulado em anos, não um certificado. O entregável final chama-se **Applied AI Engineering Capstone** (nome deliberado: nomeia a competência construída, não uma senioridade).

**Quatro verbos (a formação não os confunde):**

| Verbo | O que é | Foco da formação? |
|---|---|---|
| **Usar IA** | produtividade com ferramentas prontas | só o track curto |
| **Construir com IA** | engenharia de software com modelos prontos (APIs, RAG, tools, evals, operação) | **foco central** |
| **Treinar modelos** | ajustar/treinar com dados (ML clássico, fine-tuning) | intuição + casos onde compensa |
| **Pesquisar modelos** | criar arquiteturas, papers, matemática pesada | aponta a trilha; fora do foco |

**Como funciona de forma autodidata.** Cada módulo é self-contained, com passo a passo, comandos, fixture sintético, troubleshooting, FAQ, **self-assessment** e **exemplos de referência** que funcionam como mentores silenciosos. Você estuda, constrói, se autoavalia e **publica evidência no GitHub sozinho**. Peer review, cohort, mentoria e revisão oficial podem existir — são camadas extras, nunca pré-requisitos (Seção 5).

---

## 2. Tese central da formação

> **AI Engineering é Software Engineering com modelos probabilísticos no meio.**

Desdobramentos que governam o desenho:

- **A formação de IA não reensina engenharia genérica** — ela **reaplica** fundamentos (testes, observability, segurança, APIs, persistência) a **sistemas probabilísticos**: testes viram **evals**; logs viram **tracing de LLM com custo/token**; tratamento de erro inclui **alucinação e abstenção**; segurança inclui **prompt injection** (conteúdo externo é **dado, não comando**); persistência inclui **vector store e qualidade de retrieval**.
- **RAG não é uma camada** da IA — é uma **arquitetura** sobre LLMs. E **semantic search não é RAG**.
- **Tool calling não é Agent.** Tool calling controlado é o default; autonomia é exceção justificada.
- **Produção não é demo.** "Funcionou uma vez" nunca é "está pronto".
- **Self-paced first, cohort optional.** A formação funciona para o autodidata; o resto é camada.

---

## 3. Relação com a Polaris Academy

A formação de IA é **uma** das formações de um ecossistema **modular por dentro, trilha guiada por fora** (registry único; formações **referenciam** módulos, não copiam). Três camadas transversais sustentam tudo:

| Camada | Papel |
|---|---|
| **Technical Common Core** | fundamentos de engenharia (Git, terminal, HTTP/APIs/JSON, SQL, testes, Docker/CI, observability conceitual). Programação **conceitual/agnóstica**; **Python obrigatório só em IA**; Java/TS para SWE. DSA em quatro faixas (mínimo é comum; o resto é de SWE). |
| **Professional Core** | meta-habilidades e habilidades profissionais (Seção 4) — paridade com o Technical Common Core. |
| **Self-Paced Learning Experience** | a camada que garante estudo autodidata (Seção 5). |

**Duas formações principais:** **Software Engineering** (Júnior→Principal) e **Applied AI Engineering** (Foundations→Capstone, *rumo a Specialist*). A de IA **depende** do Common Core (= SWE Foundations) via um **Foundations Check** (placement que waiva o Common Core, **não** o `AI Foundations for Builders`).

**Common Core vs AI-specific.** Cerca de 80% dos "sistemas" da formação de IA é Common Core/SWE reaplicado; só ~20% é genuinamente AI-específico (evals, qualidade de retrieval, prompt injection, custo/token, alucinação, limites de tool).

**Decisões provisórias v0.1** (todas "aprovado para draft v0.1", revisáveis): spine de níveis nomeados; schema de módulo; **Polaris Commerce Platform** (projeto-mãe de SWE, seed booking, que alimenta o dataset do assistente de IA); **Python** como linguagem de referência do Common Core conceitual; **pgvector** como store padrão didático.

---

## 4. Professional Core

**Definição.** A terceira camada transversal: desenvolve **aprender, investigar, persistir, comunicar, decidir sob incerteza, ownership, ética e gosto de engenharia** — avaliada sobre os **mesmos artefatos técnicos** que o aluno já produz (nunca aula isolada).

**Habilidades + progressão por senioridade** (a mesma skill muda de natureza ao subir):

| Habilidade | Júnior | Pleno | Sênior | Staff/Principal |
|---|---|---|---|---|
| Aprender a aprender | segue plano dado | monta o próprio; docs primárias | domina área nova **sem curso** | define o que a org aprende |
| Debugging | lê erro, isola | reproduz; instrumenta | causa-raiz em sistema **não-determinístico** | previne classes de falha |
| Comunicação | README claro | ADR; adapta à audiência | RFC que alinha times | estratégia org-wide |
| Ownership | leva a tarefa | assume resultado e falhas | assume o sistema em operação | assume área/decisões de risco |
| Pensamento crítico | "funciona mesmo?" | desconfia de demo/benchmark | trade-offs sistêmicos | mata iniciativa ruim com dados |
| Decisão sob incerteza | escolhe com critério simples | trade-off memo | decide com info incompleta | define como a org decide |
| **Engineering Taste** *(avançada)* | — (semente) | nota fragilidade | prefere o simples por convicção | enxerga overengineering / demo-que-mascara-risco antes da dívida |

**Persistência (redefinida, sem romantizar sofrimento):** **investigação com método + troca de estratégia quando trava + pedir ajuda com contexto na hora certa.** *Excelente* = resolve o difícil com método e **sabe quando parar/pivotar é a decisão certa**.

**Learning How to Learn** inclui **gestão de rotina e energia**: planejamento semanal, estudo sustentável, anti-tutorial-hell, equilíbrio teoria↔prática, revisão espaçada, consistência (artefato: weekly plan + evolution log).

**Avaliação formativa vs bloqueante.** Todo módulo declara ≥1 habilidade; **labs = feedback formativo** (self-assessment leve, peer opcional); **checkpoints = rubrica (2–4 skills)**; **capstone = eixo profissional completo, bloqueante**.

**Como funciona para o autodidata.** A maioria das habilidades tem **proxy máquina-verificável ou exemplo de referência**: *debugging* → um Debugging Diary comparável ao 10/10; *trade-off thinking* → um ADR comparável; *engineering taste* → comparar a própria arquitetura com a reference solution e ver a complexidade desnecessária. O subjetivo que sobra é onde peer/mentor (opcional) agrega — e é declarado como tal, sem fingir que self-study resolve 100%.

---

## 5. Self-Paced Learning Experience

**Tese.** *Self-paced first. Cohort optional. Mentor optional. Review optional.* A formação funciona para estudo 100% autodidata; tudo o mais é camada extra. Peer review, cohort, mentoria e revisão oficial da Polaris podem existir no futuro, mas são opcionais.

### 5.1 Princípios

1. **Self-paced first** — o default é estudo autodidata; tudo o mais é camada extra.
2. **No hidden mentor dependency** — nenhum passo exige um humano para destravar.
3. **Every module must be self-contained** — dá para fazer o módulo isolado, com tudo que precisa alcançável a partir dele.
4. **Every checkpoint must have self-assessment** — o aluno se avalia por rubrica antes de avançar.
5. **Automation before human review** — o que dá para checar por código/lint, checa-se por código.
6. **Community as support, not dependency** — comunidade ajuda, mas a formação funciona sem ela.
7. **Examples are silent mentors** — exemplos ruim→10/10 ensinam sem ninguém presente.
8. **Reference solutions are calibration tools** — servem para comparar, não para copiar.
9. **Low-cost mode by default** — cached/mock/synthetic/modelo barato como caminho padrão.
10. **Synthetic data only** — nunca logs reais, dados de clientes, corporativos ou PII real.
11. **Progress must be visible** — o avanço aparece no repo (commits, evals, checklists), sem avaliador.

**Self-contained não significa monolítico.** *Self-contained = "tudo está disponível e navegável a partir do módulo", não "tudo no mesmo arquivo".* O empacotamento padrão de cada módulo é **uma página principal enxuta** + arquivos satélite linkados quando necessário: `lab-guide`, `troubleshooting`, `reference-solution`, `rubric`, `faq`. Critério: a partir do módulo, o aluno alcança tudo em um clique — sem depender de um humano ou de outro módulo.

### 5.2 Modos de consumo

| Modo | Como funciona | Obrigatório | Opcional | Avaliação | Evidência | Limitação | Badge/credencial |
|---|---|---|---|---|---|---|---|
| **Self-study** *(default)* | estuda e constrói sozinho, no próprio ritmo | self-assessment + bloqueadores máquina-verificáveis + comparar com reference solution | comunidade | self + automação | repo público + self-assessment | sem validação externa; risco de auto-leniência | **self-certified** = *evidência pública de aprendizado*, **não credencial oficial** |
| **Peer-reviewed** *(opcional)* | pares revisam via rubrica pública | submeter o review package | tudo o mais | peer + automação | repo + peer reviews | qualidade varia com o par | "peer-reviewed" (sinal mais forte; ainda não oficial) |
| **Cohort** *(opcional)* | turma com prazos, showcases, peer review estruturado, demo day | participar dos ritos da cohort | mentoria | peer estruturado + automação | + demo day | exige organização/tempo | cohort completion |
| **Mentored** *(opcional)* | mentor dá feedback direcionado | sessões com o mentor | cohort | mentor + automação | + feedback registrado | não escala / custo | mentored |

> **Regra dura:** *self-study completion não é certificação oficial.* É **evidência pública de aprendizado**. Qualquer badge futuro deve sinalizar **o modo** (self/peer/cohort/mentored), nunca prometer "especialista".

### 5.3 Contrato de módulo autodidata

Além dos campos do schema de módulo, todo módulo exige os campos que tornam o estudo possível sem ninguém:

```yaml
# --- Self-Paced (campos obrigatórios) ---
estimated_time: { min_h, max_h }
recommended_profile: [dev-experiente | iniciante | data-analyst | staff | produto]
what_you_build: "frase concreta do entregável"
step_by_step: "passos numerados executáveis"
commands: ["make ...", "..."]      # tudo roda por comando
dataset_or_fixture: "synthetic; caminho do fixture"
self_assessment: required          # rubrica + comparação com exemplo 10/10
worked_examples: { ruim, basico, bom, dez_de_dez }
troubleshooting: "erros comuns -> causa -> correção"
faq: "perguntas frequentes do módulo"
reference_solution: partial|full   # calibração, não cópia
next_step: "id do próximo módulo"
estimated_cost: "USD aprox. (e custo em low-cost mode)"
offline_mode: cached|mock|local    # quando possível, sem gastar token
# --- Custo (a preencher antes da publicação pública) ---
estimated_cost_low: ...
estimated_cost_live_api: ...
estimated_cost_zero_or_mock: ...
max_calls_suggested: ...
cached_mock_local_alternative: ...
```

### 5.4 Contrato de checkpoint autodidata

Todo checkpoint tem, obrigatoriamente: **o que submeter** (artefatos + repo) · **comandos para validar** (`make test`, `make eval-cached`, lint de bloqueadores) · **critérios mínimo · bom · 10/10** · **bloqueadores** (máquina-verificáveis listados) · **self-assessment** (rubrica dos dois eixos + comparação com o exemplo 10/10) · **checklist antes de avançar** · **quando pedir ajuda** · **como formular uma boa pergunta** (contexto + repro + o que já tentou + objetivo) · **como publicar evidência no GitHub** (repo público, README, commits, `evals/results/`).

### 5.5 Artefato padrão `progress.md`

Obrigatório em todo repo do aluno — torna o progresso visível sem avaliador:

```
# Progress — <aluno> · <formação>
## Módulos concluídos        # id + data
## Checkpoints               # nível -> mínimo/bom/10-10 atingido + self-assessment
## Evidências                # links: repo, evals/results/, demos
## Comandos rodados          # make ... (o que rodou e resultado)
## Commits / PRs             # links
## Dificuldades encontradas  # o que travou + como resolveu (insumo do Debugging Diary)
## Próximos passos
## Blockers                  # o que está impedindo + quando pedir ajuda
```

### 5.6 Reference solutions e exemplos (mentores silenciosos)

A Polaris cria, no mínimo: **starter repo** · **reference solution parcial** (não a resposta inteira — para não matar o aprendizado) · **exemplo ruim · básico · bom · 10/10** (do mesmo Incident Assistant) · **solution notes** (explicando os trade-offs das decisões). Para o autodidata, esses exemplos substituem o mentor: ele compara a própria entrega com a 10/10 e vê a distância sem ninguém dizer.

**Regra anti-cópia.** Reference solutions são **ferramentas de calibração, não atalhos**: **tentar primeiro** (o aluno produz a própria versão antes de abrir a referência) · **comparar depois** · **parcial antes da completa** · **solution notes explicam trade-offs** (o valor está no *porquê*, não no código pronto) · **nunca começar copiando**. O `progress.md` **desincentiva a cópia, torna a trilha de tentativa visível e ajuda o aluno a comparar processo (não só resultado)** — mas **não garante detecção automática**.

### 5.7 Study plans por ritmo

| Ritmo | Duração provável (Foundations→Capstone) | Riscos | Teoria/prática | Anti tutorial-hell | Consistência |
|---|---|---|---|---|---|
| **3h/sem** | **12–18 meses** | perder o fio; abandono | ~30/70 | 1 conceito → 1 commit por semana | sessão fixa semanal; evolution log |
| **6h/sem** | **7–10 meses** | acumular sem revisar | ~30/70 | fechar 1 milestone antes do próximo | 2 sessões/sem; revisão quinzenal |
| **10h/sem** | **5–7 meses** | burnout; pular evals | ~25/75 | nunca avançar com checkpoint vermelho | ritmo > intensidade; descanso real |

> **Dev experiente** (que waiva o Common Core via Foundations Check) pode ficar **abaixo** dessas faixas; **iniciante técnico** (que faz Common Core + Nível 1 do zero) tende a ficar **acima**. As faixas assumem o perfil "dev com base, ritmo honesto, sem pular evals". Em todos: prática domina; **nenhum nível avança com checkpoint vermelho**.

### 5.8 Low-cost / low-friction mode (default)

cached evals (`make eval-cached`) · **mock providers** (`make test`, sem token) · **datasets sintéticos** · **modelos baratos** para iterar (modelo caro só na avaliação final) · **rodar local** quando possível (ex.: pgvector em Docker; embeddings locais) · **limites de chamadas** + **budget estimado por nível** · **nenhuma cloud paga exigida no início**. Cada módulo declara `estimated_cost` e o custo em low-cost mode (campos de custo a preencher antes da publicação pública).

### 5.9 Riscos do estudo solo (e mitigações)

| Risco | Mitigação |
|---|---|
| **Auto-leniência** (o aluno se dá nota alta) | self-assessment é rubrica + **comparação com o exemplo 10/10**, não "achei bom" |
| **Erros sutis sem feedback** (ex.: "citação que não sustenta") | **bloqueadores máquina-verificáveis** pegam o objetivo; **reference solutions** calibram o subjetivo |
| **Falsa confiança (Dunning-Kruger)** | bloqueadores + exemplos âncora + sinais de falsa confiança na régua de maturidade |
| **Abandono sem accountability** | study plans + `progress.md` visível + comunidade opcional como rede de segurança |
| **Custo de API assustando** | low-cost mode default |
| **Tutorial hell** | estrutura em milestones + regra "1 conceito → 1 incremento → 1 evidência" |

> O eixo **profissional** é o mais difícil de autoavaliar sozinho. Reference solutions e proxies máquina-verificáveis **reduzem, não eliminam** — por isso peer/mentor existe como camada de sinal mais forte, **opcional**.

### 5.10 Comunidade como suporte, não dependência

Discord / GitHub Discussions / Issues ajudam com **dúvidas, peer review, showcases, feedback e cohorts futuros**. Mas a regra é inegociável: **a formação tem que funcionar mesmo se o aluno estudar 100% sozinho.** Comunidade é rede de segurança e aceleração, nunca pré-requisito.

---

## 6. Projeto-mãe

**`AI Incident & Support Assistant`** — um assistente que ajuda times a entender incidentes, logs, tickets, runbooks e próximas ações. Cenário canônico: uma **reserva de passagem** que falhou (pagamento autorizado, emissão não ocorrida, mensagem na `DLQ`, status divergente).

**Relação com a Polaris Commerce Platform.** É o sistema (da formação de SWE) que **emite** os incidentes/logs/eventos. O assistente de IA **consome um dataset sintético** derivado dele, via **contrato versionado** — sem acoplamento rígido. Integração ao vivo é **lab opcional** (só para quem fez as duas formações).

> **Regra obrigatória: `synthetic data only`.** O projeto-mãe usa **exclusivamente dados sintéticos**. **Nunca** logs reais, dados de clientes, dados corporativos ou **PII real** — nem para "ficar mais realista". Isso protege o aluno, a comunidade e a marca.

**Evolução v0 → v14** (mapeada aos níveis):

| Versões | Nível | O que ganha |
|---|---|---|
| **v0** | AI Foundations | problema, personas, domain map, `problem-framing.md`, baseline definido, EDA mínima, privacy note — **sem IA** |
| **v1–v6** | AI Builder | dados → EDA → baseline sem IA → classificador clássico → embeddings/busca semântica → **LLM com evals** |
| **v7–v9** | AI Application Engineer | RAG avaliado → tool calling controlado → **Minimum Operable API** |
| **v10–v14** | Capstone | consolidação, segurança/observability/custo endurecidos, governança documentada, **case defensável** |

---

## 7. Arquitetura geral da formação

```
[ track opcional ]      AI Literacy & Productivity   <- "usar IA"; curto; sem coding profundo
        |
        v  (Foundations Check waiva o Common Core, nao o nivel abaixo)
   Nivel 1   AI Foundations for Builders     <- camadas da IA, problem framing, metricas, dados, Responsible AI basico (v0)
   Nivel 2   AI Builder                      <- LLMs, prompting, structured outputs, APIs, EVALS desde o dia 1; ML classico+embeddings (v1->v6)
                                                milestones 2.1-2.4
   Nivel 3   AI Application Engineer          <- RAG avaliado, tool calling controlado, Minimum Operable API (v7->v9)
                                                MINI-PROGRAMA em sprints 3.1-3.5
        |
        v
   Applied AI Engineering Capstone            <- consolidacao defensavel (v10->v14); Core / Advanced / Portfolio Polish; MVP Capstone
        |
        v
   [ futuro/backlog ]  Trilhas avancadas      <- RAG · Agents · LLMOps · Responsible AI · AI Product   (NAO abertas na v0.1)
```

- **AI Literacy & Productivity** — track **curto e opcional** ("usar IA"; pode parar aqui e já ter valor).
- **Níveis 1→3** — o core de "construir com IA", do conceito à aplicação operável.
- **Nível 3 é um mini-programa em sprints** (3.1 RAG Minimum Viable → 3.2 Evaluated Retrieval → 3.3 Grounded Answer → 3.4 Controlled Tool Calling → 3.5 Minimum Operable API), não um módulo curto.
- **Applied AI Engineering Capstone** — o destino: consolidação **defensável**, em três camadas (Core/Advanced/Portfolio Polish), com **MVP Capstone** para a primeira cohort.
- **Trilhas avançadas** — **backlog pós-v0.1**; não abertas agora.

---

## 8. Padrões obrigatórios da formação

Todo nível segue o **Level Template 10/10** + os padrões de reprodutibilidade e self-paced. Esta seção é a fonte única; os níveis referenciam, não repetem.

**8.1 Estrutura de todo nível.** North Star Demo · milestones/sprints · módulos (schema) · artefatos obrigatórios · labs com **mínimo/bom/10-10** · anti-patterns · Professional Core embutido · **self-assessment** · troubleshooting · **reference solutions** · caminhos por perfil · materiais diversos verificados · reprodutibilidade · critério UAU · prompt-tutor · checkpoint de dois eixos.

**8.2 Artefatos — regra geral.** Todo artefato tem objetivo · template · exemplo **ruim/bom/10-10** · critérios de aceite · rubrica · papel no portfólio. Empacotamento **self-contained ≠ monolítico** (página enxuta + satélites linkados).

**8.3 Reprodutibilidade (obrigatória).**
- Comandos `make` claros; **três modos de eval:** `make eval-live` (provider real), `make eval-cached` (resultados salvos), `make test` (mocks/smoke, **sem token**).
- **Run manifest** em todo eval: `provider · model · version/date · temperature · max_tokens · prompt_version · embedding_model · custo_estimado · timestamp` → gravado em `evals/results/`.
- **Dev vs holdout:** `dev-set.jsonl` para iterar; `golden/holdout-set.jsonl` só para avaliação final. **Otimizar no holdout = overfitting** (anti-pattern).
- **`progress.md`** mantido; **árvore esperada do repo** por nível.

**8.4 Segurança com evidência.** Checklist por nível **com prova executável** (não "tomei cuidado"); `provider-policy-note.md` + teste de masking/redaction; **conteúdo externo é dado, não instrução**; **synthetic data only**.

**8.5 Avaliação em dois eixos + self-paced.** **Technical** + **Professional**; **formativo nos labs**, **rubrica no checkpoint**, **bloqueante no Capstone**. Todo checkpoint traz **self-assessment** + comparação com o **exemplo 10/10**, **bloqueadores máquina-verificáveis**, e "como publicar evidência".

**8.6 Materiais — regras de curadoria.** Diversidade (oficial · institucional · indústria · independente · opcional avançado); **separar a trilha do aluno da do instrutor**; **link canônico ou "a verificar"** em todo item; **nunca framework como primeira fonte**.

---

## 9. Nível 1 — AI Foundations for Builders

**Resumo.** Fundação **conceitual e de dados** de quem vai construir com IA: mapa das camadas (com a errata da imagem de origem), problem framing, métricas/avaliação, dados + estatística mínima, Responsible AI básico + privacidade. **Sem LLM, sem chatbot, sem RAG.** Instala a disciplina central: definir sucesso antes de construir.

**Objetivo.** Sair de "IA é mágica" para "sei enquadrar um problema, escolher métrica, definir baseline sem IA e reconhecer leakage/PII".

**Pré-requisitos.** Obrigatório: Common Core A (ou Foundations Check) + Python básico. Recomendado: Common Core B (incident thinking). O Foundations Check waiva o Common Core, **não** este nível.

**North Star Demo.** Receber o **dataset sintético** de incidentes e produzir `problem-framing.md` (ideal outcome × model goal × success metric de negócio + **baseline sem IA**), uma EDA mínima e uma `privacy-note.md`. O UAU, mesmo conceitual, é perceber com um exemplo próprio **por que 95% de acurácia pode ser péssimo** — e responder "isto precisa de IA?".

**Módulos** (`professional_skill` entre parênteses):

| Módulo | Outcomes | Erro comum |
|---|---|---|
| **F1 Mapa das Camadas** *(pensamento crítico)* | explica IA/ML/DL/GenAI/LLM com exemplo próprio; **por que RAG/Agents não são camadas** | "GenAI = IA"; "Agent é um tipo de IA" |
| **F2 Problem Framing** *(decisão sob incerteza)* | `problem-framing.md`; define baseline sem IA; "precisa de IA?" | pular para "usar um LLM" sem baseline |
| **F3 Métricas e Avaliação** *(pensamento crítico)* | escolhe precision/recall/F1 pelo custo do erro; lê confusion matrix | reportar só accuracy |
| **F4 Dados + Estatística Mínima** *(atenção a detalhes)* | EDA básica; identifica **data leakage** | concluir sobre dados não inspecionados |
| **F5 Responsible AI Básico + Privacidade** *(ownership/ética)* | identifica **PII**; o que não enviar a um modelo | tratar Responsible AI como enfeite |

**Lab.** *"Framing & Baseline do Incident Assistant"* — `mínimo` produz framing + métrica; `bom` + baseline + EDA + leakage; `10/10` + trade-off memo "precisa de IA?" + PII marcada. Produz a **v0** do projeto-mãe. Self-assessment leve (formativo).

**Artefatos.** `problem-framing.md` · `eda-notebook` · `privacy-note.md` · `model-card.md` (intro) · `README.md` · `progress.md`.

**Materiais** (verificados; aluno vs instrutor — revalidar antes da publicação pública):
- *Aluno:* **Elements of AI** (`elementsofai.com`) · **Google ML Crash Course — Problem Framing + Classification** (`developers.google.com/machine-learning`) · **StatQuest** (YouTube).
- *Instrutor:* **Google People + AI Guidebook** (`pair.withgoogle.com/guidebook`) · **Intro to Responsible AI** (Google).
- *Complementar:* **"AI for Everyone"** (DeepLearning.AI) — *link a verificar*. · Apêndice Polaris (errata das camadas).

**Checkpoint (2 eixos).** *Técnico:* framing + baseline + métrica justificada + EDA + leakage/PII. *Profissional:* pensamento crítico ("precisa de IA?") + atenção a detalhes + decisão (trade-off memo). **Mínimo/bom/10-10** explícitos; self-assessment + comparação com exemplo 10/10. **Bloqueador:** sem baseline definido / sem métrica justificada.

**Critério UAU.** *Fez o tutorial:* "leu sobre IA". *Fez bem:* framing + baseline + métrica certa. *10/10:* defende **por que** o baseline existe e qual métrica usar, identifica leakage e PII, e argumenta **onde uma regra simples bate o LLM** — tudo publicado no repo.

---

## 10. Nível 2 — AI Builder

**Resumo.** "Sei usar ChatGPT" → "sei **construir** com LLM **de forma medida**": APIs, prompting de engenharia, structured outputs com validação, custo/latência, e o coração — **evals desde o dia 1**. Em paralelo, ML clássico no mínimo e embeddings como **ponte para RAG**.

**Pré-requisitos.** Nível 1 + Common Core A/B.

**North Star Demo.** Dado um incidente, gerar **resumo + evidências + próxima ação** via LLM e **provar que é bom**: golden set, taxa de acerto, custo/latência rastreados, alucinações analisadas, e um **classificador clássico de severidade** como baseline. O UAU é ver o **eval pegar uma regressão** e o **baseline ganhar/perder do LLM com números**.

**Milestones (mini-programa):**

| Milestone | Objetivo | Critério de avanço |
|---|---|---|
| **2.1 LLM App Minimum Viable** | LLM funciona ponta a ponta (JSON validado) | saída parseável em ≥1 incidente; roda por comando |
| **2.2 Evaluation First** | "parece bom" → **medido** | `make eval` gera report com pass rate, custo/latência, ≥3 falhas; **rule-based + human review amostral** |
| **2.3 Baseline vs LLM** | provar se a IA **agregou** | decisão por ≥4 critérios + gatilho de reversão; sabe onde **não** usar LLM |
| **2.4 Embeddings as Bridge to RAG** | embeddings **só como ponte** | semantic vs keyword medido; reconhece que **isto não é RAG** |

**Módulos.** B1 LLM Fundamentals (tokens/context window/latência) · B2 Prompting de Engenharia (**task decomposition, evidence-based outputs, concise rationale, structured reasoning fields** — sem depender de "cadeia de raciocínio" como truque) · B3 Structured Outputs (validar no código) · B4 APIs de LLM (auth/streaming/rate limits/retries) · **B5 Evals desde o dia 1** (golden set, rule-based **obrigatório**, human review amostral **obrigatório**, LLM-as-judge **recomendado/opcional, sinal complementar, nunca verdade final**) · B6 ML Clássico mínimo + Baseline vs LLM · B7 Embeddings & Busca Semântica.

**Embeddings (regra do nível).** semantic search **≠** RAG; vector store **não resolve conhecimento**; top-k parecido **≠** resposta correta; **comparar com keyword search** e **medir se embeddings agregaram** (entregar `embeddings-evaluation.md`, com conclusão honesta — às vezes keyword bastava).

**Labs (mín/bom/10-10).** *Baseline vs LLM Showdown* · *Build & Measure the Incident Summarizer* · *Semantic Search de Incidentes*.

**Anti-patterns.** prompt que parece bom mas não é testável · LLM sem baseline · **structured output sem validação** · golden/eval enviesado · **confiar cegamente no LLM-as-judge** · embeddings sem entender retrieval · framework antes da API crua · ignorar (ou otimizar cedo demais) custo.

**Reprodutibilidade.** `make install/test/eval/eval-cached/eval-live/report/demo`; `Makefile`, `.env.example`, `pyproject.toml`/`requirements.txt`, `evals/run_eval.py`, `evals/results/`, `tests/`, `evals/labeling-guidelines.md`. **Dev-set vs holdout**; **run manifest**. Se `make eval` não roda num clone limpo, o milestone 2.2 **não fecha**.

**Security checklist** (`security/ai-builder-safety-checklist.md`, com evidência). sem key commitada · `.env.example` · **PII mascarada** · minimização de dados · **separar input externo de instrução** · validar output · logar sem segredo · documentar provider/modelo. Acompanha `provider-policy-note.md` + teste de redaction.

**Artefatos.** `evals/eval-report.md` · `evals/golden-set.jsonl` + `evals/labeling-guidelines.md` · `prompts/*.md` (versionados) · `decisions/ADR-002-baseline-vs-llm.md` · `model-card.md` · `embeddings-evaluation.md` · `README.md` · `progress.md`.

**Checkpoint (2 eixos).** *Técnico:* eval-report (golden + métricas + custo/latência + falhas) + structured output validado + ADR baseline-vs-LLM + busca semântica avaliada. *Profissional:* pensamento crítico (quando não usar LLM) + trade-offs (ADR) + atenção a detalhes (review do golden) + ownership (eval-report). **Mín/bom/10-10**; self-assessment + exemplo 10/10. **Bloqueadores:** sem golden set / **prompt de LLM sem eval** / key commitada.

**Critério UAU.** *Tutorial:* o LLM responde. *Bem:* golden set + métricas + structured output validado + baseline comparado + custo conhecido. *10/10:* o eval **pega regressão**; a decisão baseline-vs-LLM é **defensável com números e gatilho de reversão**; alucinação analisada; o aluno **conhece os limites do próprio eval** e diz **com dados onde o LLM não deveria estar**.

---

## 11. Nível 3 — AI Application Engineer

**Resumo.** O assistente vira **aplicação de IA operável e medida**: ingere documentação operacional, **recupera evidência (e mede se acertou)**, gera respostas **com citações e limites**, usa **tool calling controlado (tool calling não é Agent)** e expõe uma **Minimum Operable API**. A régua passa a incluir medição de **retrieval** e **grounding**.

> **Mini-programa em sprints, não módulo curto.** É o maior salto da formação e deve ser executado como mini-programa: um sprint por milestone, cada um com entregável e checkpoint próprios. **Nenhum sprint avança com checkpoint vermelho.** *Duração sugerida (a validar): a 6h/semana, da ordem de 1–2 semanas por sprint, ~6–10 semanas no nível; mais rápido para dev experiente, mais lento para iniciante.*

**Pré-requisitos.** Nível 2 + Common Core A/B.

**North Star Demo.** Incidente → ingere runbooks/postmortems → recupera evidência certa (`precision@k`/`recall@k` medidos) → responde **citando** e diz **"não sei"** quando a doc não cobre → **tool read-only** (validada, auditada) → `POST /incident-assistant/analyze` com timeout/retry/**tracing**/custo. E **defende com dados quando RAG/tool calling NÃO valem a pena**.

**Sprints (milestones):**

| Sprint | Objetivo | Critério |
|---|---|---|
| **3.1 RAG Minimum Viable** | 1º RAG funcional sobre runbooks/postmortems | roda ponta a ponta; ainda não confiável |
| **3.2 Evaluated Retrieval** | provar se o retrieval acha a evidência certa **antes** da geração | P@k/R@k mostram melhora/piora; keyword vs semantic vs hybrid comparados |
| **3.3 Grounded Answer Generation** | respostas que **citam** e abstêm | cita evidência real, **não inventa**, abstém sem evidência |
| **3.4 Controlled Tool Calling** | tool calling controlado — **não Agent** | tool certa quando precisa, **não** quando não precisa; valida I/O; audita |
| **3.5 Minimum Operable API** | expor como API **operável** | roda local por comando; **previsível em erro**; tracing + custo |

> **Refinamentos:** reranking/hybrid são "**medir, adotar só se merecer**" (anti-overengineering); **3.2 é o portão** (não gere sobre retrieval não medido); **3.4 reusa o dataset/contrato da Polaris Commerce Platform** (universo conectado).

**Módulos.** C1 Ingestion & Chunking (controlado, metadata) · C2 Retrieval & Vector Stores (**pgvector**; keyword/semantic/hybrid; rerank introdutório) · C3 Retrieval Evaluation (P@k/R@k, top-1 útil, **dev vs holdout**) · C4 Grounded Answer Generation (grounding, citations, faithfulness, **abstenção**) · C5 Controlled Tool Calling (schema, validação, **idempotência**, allowlist, audit, "result = dado", fallback) · C6 Minimum Operable API (FastAPI, timeout/retry/error, schemas, logging sem PII, tracing, custo, healthcheck) · C7 AI App Security (prompt/tool injection, data exfiltration, PII masking, **external = data not instruction**, output validation).

**Labs (mín/bom/10-10).** *Retrieval Showdown* (keyword vs semantic vs hybrid) · *Grounded Answer with Abstention* · *Controlled Tool Calling* (com **resistência a injection**).

**Anti-patterns.** chamar semantic search de RAG · "vector DB resolve conhecimento" · chunking aleatório · não medir retrieval · top-k sem avaliar · responder sem citar · citação que não sustenta · **RAG para dado que é de banco** · tool sem validação/idempotência · **chamar tool calling de Agent** · framework antes das primitivas · não separar dado externo de instrução · logar PII · não saber dizer "não sei".

**Artefatos.** `docs/rag-architecture.md` · `docs/corpus-versioning.md` · `decisions/ADR-003-rag-stack.md` · `evals/retrieval-labeling-guidelines.md` · `evals/retrieval-eval-report.md` · `evals/rag-eval-report.md` · `evals/rag-failure-taxonomy.md` · `tools/tool-contracts.md` · `tools/orchestration-policy.md` · `security/rag-tool-safety-checklist.md` · `security/document-access-policy.md` · `observability/ai-app-tracing.md` · `observability/cost-guardrails.md` · `README.md` · `progress.md`.

- **`corpus-versioning.md`:** `document_id/source/version/last_updated/content_hash/ingestion_ts/status`; **delta reindex**; invalidar chunks antigos; **conflito → preferir recente + sinalizar**; **proveniência por resposta**.
- **`document-access-policy.md`:** `access_level` como metadata; **filtrar no retrieval, não na resposta**; logs sem conteúdo protegido. Obrigatório agora: filtro simples + teste de não-vazamento. RBAC/multi-tenant → Responsible AI/LLMOps.
- **`rag-failure-taxonomy.md`:** retrieval miss/noise · wrong chunk boundary · stale doc · conflicting evidence · citation mismatch · unsupported claim · over-answering · failed abstention · unnecessary/wrong tool call · tool result misread (como aparece / detectar / corrigir).
- **`orchestration-policy.md`:** resposta direta · RAG · tool · "não sei" · human-in-the-loop (futuro). Regras: **status → tool/banco, não RAG**; procedimento → RAG; sem evidência → "não sei"; **tool read-only; nenhuma destrutiva no Nível 3**; resultado = dado.

**Reprodutibilidade.** `make install/ingest/retrieval-eval/rag-eval/tool-eval/api/demo/test` + `eval-live/cached`; `evals/results/` com run manifest; **árvore do repo** completa no nível.

**Materiais** (verificados; diversos; framework **não** como 1ª fonte — revalidar antes da publicação pública):
- *Aluno:* **pgvector** (`github.com/pgvector/pgvector`, oficial) · **Ragas** (conceitos de métricas — *URL canônica a verificar*) · **Anthropic "Building effective agents" + tool use** (`anthropic.com/engineering/building-effective-agents`) · **FastAPI** · **OpenTelemetry**.
- *Instrutor:* **Chip Huyen "AI Engineering"** (caps RAG/avaliação) · **DeepLearning.AI "Building and Evaluating Advanced RAG"** (RAG triad) · **Jason Liu "Systematically Improving RAG"**.
- *Independente:* **"What We Learned from a Year of Building with LLMs"** · **Encore "You probably don't need a vector database"** · **Simon Willison** (*URL a verificar*).
- *Complementar crítico (depois das primitivas):* **LangChain/LlamaIndex** — adotar de propósito, não por moda.

**Checkpoint (2 eixos).** *Técnico:* retrieval-eval (P@k/R@k + comparação) + rag-eval (faithfulness + citação + abstenção) + tool-contracts/test_tools + API operável com tracing/custo + safety-checklist com evidência (injection + masking). *Profissional:* Engineering Taste (overengineering?) + trade-offs (ADR-003) + ownership (limites/"não sei"/custo) + atenção a detalhes (citações/schemas). **Mín/bom/10-10**; self-assessment + exemplo 10/10. **Bloqueadores:** RAG sem citação / retrieval não medido / key ou PII vazada / injection trivial passa.

**Critério UAU.** *Não é "chatbot com PDF".* **10/10:** `make ingest · retrieval-eval · rag-eval · api · demo` rodam num clone limpo; retrieval **medido e comparado** (conclusão honesta); resposta **cita evidência correta** e **diz "não sei"**; tool calling **controlado, validado, idempotente, auditável e resistente a injection**; **segurança testada**; custo/latência conhecidos; e o aluno **defende quando RAG/tool calling são úteis e quando são overengineering**.

---

## 12. Applied AI Engineering Capstone

**Nome final.** `Applied AI Engineering Capstone`. Nomeia a **competência construída**, não uma senioridade. "Specialist" é **direção de maturidade**, não promessa de título. O Capstone é **evidência de prontidão (readiness)**, não certificado.

**Objetivo.** Entregar a versão final do *AI Incident & Support Assistant* (v10→v14) e **defendê-la**. Não precisa ser SaaS; precisa ser **operável, medido, seguro, documentado e defensável** numa entrevista ou revisão de arquitetura. Não introduz conteúdo novo — **integra, endurece e defende** o que foi construído nos Níveis 1–3.

**North Star Capstone Demo.** Alguém que nunca viu o projeto **clona e roda `make demo`** e vê: incidente → retrieval medido → resposta **com citações** e **"não sei"** quando cabe → **tools read-only** auditadas → API operável com **tracing e custo** → um **case study** com arquitetura, decisões, **falhas, custo e limites**. Em ~4 min de vídeo, **cada decisão é defensável** — inclusive *onde a IA não entra*.

### 12.1 Três camadas

| Camada | Função | Artefatos |
|---|---|---|
| **Capstone Core** *(obrigatório p/ concluir)* | o sistema **defensável mínimo** | `README.md` · `docs/architecture.md` (simples) · `evals/retrieval-eval-report.md` · `evals/rag-eval-report.md` · `evals/tool-calling-eval-report.md` (1 tool read-only) · `security/final-security-checklist.md` (básico, com evidência) · `observability/cost-report.md` (simples) · ≥1 `decisions/ADR-*.md` · `docs/limitations.md` · `make demo` + `make eval-cached` + demo curta · `professional-core/evidence.md` (enxuto) · `progress.md` |
| **Capstone Advanced** *(entrega muito forte)* | profundidade que separa "passou" de "excelente" | `docs/system-card.md` · `evals/final-eval-report.md` · `security/risk-register.md` + `document-access-policy` testado · `observability/final-observability-report.md` + cost-guardrails · `corpus-versioning` com proveniência · `tools/orchestration-policy.md` · keyword/semantic/hybrid (+ rerank avaliado) · `eval-live` reproduzível · injection **testada** |
| **Portfolio Polish** *(recomendado p/ publicar)* | vitrine | `docs/portfolio-case-study.md` · `docs/demo-script.md` + vídeo 3–5 min editado · README com diagramas · post de blog/LinkedIn · releases datadas · pitch de entrevista (30s) |

> **Core conclui** (com bloqueadores verdes). **Advanced** eleva a nota. **Polish** é para o mundo ver (não conta na graduação).

### 12.2 MVP Capstone (1ª cohort)

Menor entrega defensável (= Core enxuto): `README.md` · `make demo` · `make eval-cached` · `docs/architecture.md` simples (1 diagrama) · `retrieval-eval-report.md` (P@k/R@k vs keyword) · `rag-eval-report.md` (faithfulness + citação + 1 caso de "não sei") · **uma tool read-only** validada · `final-security-checklist.md` básico (sem key, PII mascarada, output validado — com evidência) · `cost-report.md` simples · **um** ADR · demo curta (com 1 falha mostrada).

**Fora do MVP** (vai para Advanced/Polish): system-card, risk-register, final/consolidated reports, traces por etapa, cost-guardrails completo, corpus-versioning + proveniência, document-access testado, hybrid/rerank, `eval-live`, injection testada, case study/vídeo/post. **Os bloqueadores valem inclusive no MVP.**

### 12.3 Modos do Capstone (self-paced)

| Modo | O que muda | Evidências |
|---|---|---|
| **Self-certified** *(default)* | aluno roda bloqueadores máquina-verificáveis, preenche self-assessment com a rubrica de pesos, compara com o exemplo 10/10, publica | repo + `submission/` + self-assessment + demo |
| **Peer-reviewed** *(opcional)* | ≥1 par revisa via rubrica + bloqueadores | + `reviewer-notes.md` |
| **Polaris-reviewed** *(futuro/opcional)* | revisão oficial, se existir | + selo oficial |

**O que cada modo permite comunicar publicamente:**

| Modo | Pode comunicar | Não pode comunicar |
|---|---|---|
| **Self-certified** | "Concluí o Applied AI Engineering Capstone (self-certified) — evidência pública no GitHub" | "Sou certificado/especialista pela Polaris" |
| **Peer-reviewed** | "Applied AI Engineering Capstone revisado por pares (peer-reviewed)" | "Sou certificado/especialista pela Polaris" |
| **Polaris-reviewed** *(futuro)* | "Applied AI Engineering Capstone revisado pela Polaris" (selo oficial) | "Especialista certificado" (o selo nomeia o modo, não promete título) |

**Anti-inflação.** self-certified = "**eu** verifiquei e publiquei" (**evidência pública, não credencial**); os outros = "**outros** verificaram". O selo **sempre nomeia o modo**.

### 12.4 Bloqueadores (três classes)

| Classe | Quem checa | Exemplos | Tipo de check |
|---|---|---|---|
| **Machine-checkable** | lint/CI/scan (vale no self-study) | key/segredo commitado | **secret scan** |
| | | PII enviada sem masking | **redaction test** |
| | | `make demo` não roda em clone limpo | **make demo** |
| | | nenhum eval reproduzível | **make eval-cached** (presença + execução) |
| | | RAG sem citação / injection trivial passa | **lint/test** (assert de citação; teste de injection) |
| | | log com PII/segredo | **log check** |
| **Human-review** | par/mentor/Polaris (opcional) | citação que **não sustenta** a afirmação · qualidade da abstenção · chunking/metadata sensatos · clareza da documentação | revisão humana |
| **Defense** | defesa técnica | **não sabe explicar onde NÃO usar IA** · não justifica trade-offs sob pergunta · não reconhece limites/falhas · **tool destrutiva sem human-in-the-loop** | sessão de defesa |

> Bloqueador de qualquer classe **reprova até corrigir**, independentemente da nota. Os machine-checkable são o **gate de honestidade** do self-study. No Capstone, tool destrutiva não deveria existir; se existir, exige human-in-the-loop documentado.

### 12.5 Rubrica final com pesos

| Dimensão | Peso |
|---|---|
| Reprodutibilidade | 15% |
| Evals / retrieval / grounding | 20% |
| Arquitetura e código | 10% |
| Segurança e privacidade | 15% |
| Observability e custo | 10% |
| Documentação | 10% |
| Defesa técnica | 15% |
| Professional Core | 5% |

**Graduação:** ≥60% global **E** ≥"Bom" em cada eixo (não compensa segurança ruim com código bonito). Defesa (15%) + Professional Core (5%) carregam o eixo profissional.

### 12.6 Review package

```
submission/
├── capstone-summary.md   # 1 pagina: problema, o que construiu, resultados-chave, limites
├── demo-link.md          # link do video + instrucoes exatas (make ...)
├── review-checklist.md   # checklist do Core + bloqueadores, com link a evidencia
├── self-assessment.md    # autoavaliacao nos dois eixos ANTES do peer
└── reviewer-notes.md     # nota por dimensao, bloqueadores, feedback acionavel
```

`capstone-summary` orienta o revisor em 2 minutos; `demo-link` garante que dá para rodar; `review-checklist` torna a revisão objetiva; `self-assessment` puxa a responsabilidade para o aluno e reduz a carga do revisor; `reviewer-notes` padroniza o feedback. Operacionaliza o peer review por cohort sem sobrecarregar.

### 12.7 Demo pública (3–5 min)

Problema (incidente) → RAG medido (citação + um "não sei") → tool calling controlado (audit log; não chama quando não precisa) → operável + medido (trace por etapa + custo/latência) → maturidade (**uma falha conhecida** + número do eval + uma decisão de **não** adicionar complexidade) → limites e **quando não usar IA**. Regra: a demo mostra uma falha de propósito.

### 12.8 Portfolio packaging

Repo público (README forte, releases datadas, `decisions/` e `evals/results/` visíveis) · `portfolio-case-study.md` → post (sem hype) · vídeo embedado · pitch de 30s.

### 12.9 Exemplos de referência (backlog obrigatório)

A Polaris cria, do **mesmo** Incident Assistant: **ruim · básico · bom · 10/10** + **solution notes**. São mentores silenciosos que calibram aluno e avaliador (detalhe na Seção 17).

### 12.10 Critério UAU

*Não é "chatbot com PDF".* **10/10:** clona e roda com comandos claros · evals reproduzíveis (`eval-live/cached/mock` + manifest) · decisões documentadas (ADRs) · **mostra falhas e limites** · mede custo/latência · **segurança mínima testada** · **sabe se recusar** · usa RAG/tools com critério · **mostra quando não usar IA** · demo curta com uma falha real · README forte · case study publicável · **defensável numa entrevista ou revisão de arquitetura**.

---

## 13. Rubricas

Escala única, **5 níveis: Insuficiente · Básico · Bom · Muito bom · Excelente.** Âncora: *Básico = "fez o tutorial"; Excelente = "maturidade real". "Funcionou uma vez" nunca passa de Básico.*

**13.1 Technical Competence** — avalia: arquitetura · código · testes · evals · retrieval · grounded generation · tool calling · segurança · observability · custo · reprodutibilidade · documentação.
- *Básico:* roda no caminho feliz; pouco medido.
- *Excelente:* tudo reprodutível (clone limpo + `make`), retrieval comparado, abstenção correta, tools auditadas + injection testada, observability diagnosticável, custo com guardrails, docs que um terceiro entende.

**13.2 Professional Competence** — avalia: aprender a aprender · debugging · atenção a detalhes · comunicação técnica · trade-off thinking · ownership · engineering taste · decisão sob incerteza · explicar limitações · **dizer "não sei" e "não usar IA aqui"**.
- *Básico:* descreve o que fez.
- *Excelente:* defende decisões sob perguntas duras, mostra falhas e custo, reconhece o que faria diferente, e **argumenta com dados onde a IA não deveria estar**.

**13.3 Self-Paced Completion** *(modo self-study)* — não é credencial; é **evidência pública**.
- *Insuficiente:* repo incompleto; bloqueadores vermelhos.
- *Básico:* roda; self-assessment preenchido; bloqueadores máquina-verificáveis verdes.
- *Bom:* + evals reproduzíveis + comparação honesta com o exemplo de referência.
- *Muito bom:* + segurança testada + custo conhecido + decisões documentadas.
- *Excelente:* nível Capstone 10/10, autoavaliado e publicado (com `progress.md` mostrando a trilha de tentativa).

**13.4 Bloqueadores e critérios mínimos.** Bloqueadores (três classes, Seção 12.4) reprovam até corrigir. Mínimo de avanço por nível: checkpoint dos **dois eixos** ≥ "Bom" + bloqueadores verdes + self-assessment feito. **Nenhum nível avança com checkpoint vermelho.**

---

## 14. Caminhos por perfil

A **Seção 0 "Comece aqui"** dá o roteamento inicial (próximos 30 minutos, primeiro arquivo, primeiro comando, primeira evidência, principal risco). Abaixo, o plano por perfil — o que estudar, o que pular e o risco principal. Os comandos respeitam a regra: nada que dependa de versão futura do projeto.

- **Dev experiente.** Foundations Check waiva o Common Core; Foundations rápido → **Nível 2 (foco em evals)** → Nível 3. *Pula:* fundamentos genéricos. *Risco:* tratar LLM como "só mais uma API" e pular evals.
- **Iniciante técnico.** Common Core → Nível 1 → 2 → 3, no ritmo. *Não pula nada.* *Risco:* tutorial hell; pular o baseline.
- **Data analyst / data scientist.** Foundations Check + Common Core B; **pula o módulo de ML clássico**; foco na **engenharia** (structured output, APIs, tool calling, evals de LLM ≠ métricas de modelo). *Risco:* subestimar que a lacuna é engenharia. *Objetivo de portfólio:* **aplicação de IA operável e medida**, não notebook.
- **Staff / principal.** Nível 2 rápido → Nível 3; foco em **ADRs, Engineering Taste (overengineering), segurança e build-vs-buy**. *Risco:* pular a mão-na-massa e perder intuição de custo/falha.
- **Produto / negócio.** `AI Literacy` + Foundations conceitual; foco em problem framing, métricas e quando usar IA. *Pula:* os módulos técnicos do Nível 3. *Risco:* liderar sem entender evals.
- **Pessoa não técnica em AI Literacy.** Só o track curto; sem coding profundo. *Risco:* achar que está "construindo".

---

## 15. Materiais e curadoria

> **Os links e materiais precisam ser revalidados antes de qualquer publicação pública.** Itens marcados "a verificar" não devem ir ao ar sem checagem; itens canônicos devem ser reconfirmados na data de publicação. Currículo de IA apodrece rápido — revalidação é parte do processo.

**15.1 Regras de curadoria.** Diversidade (oficial · institucional · indústria · independente · opcional avançado); **separar a trilha do aluno da do instrutor**; **link canônico ou "a verificar"** em todo item; **nunca framework como primeira fonte**; **evitar concentração em um único fornecedor**; preferir **conceito a ferramenta** (a ferramenta muda).

**15.2 Essenciais por nível** (verificados em jun/2026):

| Nível | Aluno (essencial) | Instrutor/mentor |
|---|---|---|
| **1 Foundations** | Elements of AI · Google ML Crash Course (Problem Framing + Classification) · StatQuest | Google People + AI Guidebook · Intro to Responsible AI (Google) |
| **2 AI Builder** | Doc oficial do provedor (tutorial + structured outputs) · Hugging Face LLM Course · DeepLearning.AI short courses | Chip Huyen "AI Engineering" · "What We Learned from a Year of Building with LLMs" |
| **3 Application Engineer** | pgvector (oficial) · Ragas (conceitos) · Anthropic "Building effective agents" + tool use · FastAPI · OpenTelemetry | Chip Huyen (caps RAG/avaliação) · DeepLearning.AI "Building & Evaluating Advanced RAG" · Jason Liu "Systematically Improving RAG" |

**15.3 Independentes de alta qualidade.** "What We Learned…" · Jason Liu · Encore "You probably don't need a vector database" · Simon Willison's blog.

**15.4 A verificar** (revalidar antes da v1). "AI for Everyone" (DeepLearning.AI) · URL canônica do Ragas · URLs específicas do Simon Willison · gratuidade/links dos DeepLearning.AI short courses.

**15.5 Framework depois das primitivas.** LangChain/LlamaIndex **só como complementar crítico** após o aluno saber fazer sem framework. Multi-agent / Agents avançados / fine-tuning → backlog (trilhas).

**15.6 Para estudo autodidata.** Priorizar materiais **gratuitos e self-paced**; em low-cost mode, preferir docs oficiais + cursos práticos gratuitos; livros (Chip Huyen) como aprofundamento, não bloqueio.

---

## 16. Decision logs consolidados

**16.1 Aprovadas (v0.1).**
- Modular por dentro / trilha guiada por fora, **registry único**.
- **Tese:** AI Engineering = SWE com modelos probabilísticos; IA **reaplica** (não reensina) fundamentos.
- Common Core em **três tiers**; **programação conceitual/agnóstica**; **Python obrigatório só em IA**; Java/TS para SWE; **DSA em quatro faixas**.
- **Professional Core** como 3ª camada transversal (paridade); persistência redefinida; **Engineering Taste**; formativo → checkpoint → bloqueante.
- **Self-Paced Learning Experience** como camada oficial: *self-paced first, cohort/mentor/review optional*; **synthetic data only**.
- Taxonomia **Trilha ≠ Formação**; Checkpoint e Projeto-mãe de 1ª classe.
- Projeto-mãe **AI Incident & Support Assistant**; **Polaris Commerce Platform** (SWE) conectada via **dataset/contrato versionado**.
- **Schema de módulo** + campos self-paced (incl. `progress.md`); reprodutibilidade (`eval-live/cached/mock` + run manifest; dev vs holdout).
- Níveis nomeados: `AI Literacy & Productivity` (track) → `AI Foundations for Builders` → `AI Builder` → `AI Application Engineer` → **`Applied AI Engineering Capstone`** → trilhas (backlog).
- Nível 3 = **mini-programa em sprints**; API = **Minimum Operable** (não "Production").
- **Applied AI Engineering Capstone** como nome final; **"Specialist" = direção, não título**.
- Capstone em **três camadas** + **MVP** + **três modos** (self/peer/Polaris) + **rubrica com pesos** + **bloqueadores em três classes** + **review package**.

**16.2 Provisórias** ("aprovado para draft v0.1", revisáveis). spine de níveis · schema · **Polaris Commerce Platform** (nome/seed booking) · **Python** de referência do Common Core · **pgvector** como store padrão didático · faixas dos study plans · **campos de custo do low-cost mode** (a preencher).

**16.3 Adiadas** (decidir quando o conteúdo existir). plataforma de entrega (LMS/GitHub/Discord) · mecânica de badges/certificados · detalhamento interno da **formação de SWE** · trilhas avançadas de IA · exemplos de referência (criar) · valores de custo.

**16.4 Riscos conhecidos.** auto-leniência no self-study (mitigado por bloqueadores + exemplos de referência, **não eliminado**); eixo profissional difícil de autoavaliar sozinho; materiais de IA **apodrecem rápido** (cadência de revisão + preferir conceito a ferramenta); risco de a Academy virar repositório abandonado (operating model: domain owners, `last_reviewed`, carga distribuída); over-promise de título (mitigado por nomenclatura honesta).

---

## 17. Backlog pós-v0.1

Não construir agora; registrar. **Prioridade alta** marcada — são os itens que mais fortalecem a experiência self-paced e a calibração de qualidade.

- **[ALTA] Starter repo** (Incident Assistant + por lab).
- **[ALTA] Reference solutions** parciais + **solution notes**.
- **[ALTA] Exemplos de referência:** ruim · básico · bom · **10/10**.
- **[ALTA] Troubleshooting guides** por módulo.
- **[ALTA] Custos estimados por nível/módulo:** `estimated_cost_low / live_api / zero_or_mock`, `max_calls_suggested`, alternativa cached/mock/local.
- **Trilhas avançadas:** `RAG` · `Agents` · `LLMOps` · `Responsible AI` · `AI Product` (mesmo padrão 10/10).
- **Material didático real** (≠ documento canônico): module pages · lab guides · FAQs · templates.
- **Formação de Software Engineering** (Júnior→Principal) detalhada.
- **Camadas opcionais:** cohorts · review process · mentoria · office hours · badges/certificados (sempre nomeando o modo).
- **Estrutura de repositório** da Polaris Academy (monorepo de currículo + starters) — quando for gerar arquivos reais.

---

## 18. Auditoria crítica final

**18.1 O que está forte.**
- Anti-hype consistente: evals cedo, "RAG não é camada", "tool calling não é Agent", "produção não é demo", **synthetic data only**, e a coragem de ensinar **quando não usar IA**.
- **Dois eixos avaliados** (técnico + profissional) com âncoras tutorial-vs-maturidade.
- **Reprodutibilidade real** (clone limpo + `make`, run manifest, dev vs holdout) e **segurança com evidência**.
- **Self-paced first** com bloqueadores máquina-verificáveis e exemplos de referência como mentores silenciosos.
- Projeto-mãe único e realista, conectado ao ecossistema sem acoplamento rígido.

**18.2 O que ainda é risco.**
- **Autoavaliação do eixo profissional** sem humano — proxies reduzem, não eliminam.
- **Curadoria apodrece** (IA muda rápido) — exige cadência de revisão.
- **Custo de API** ainda **não quantificado** (campos no backlog).
- **Exemplos de referência ainda não existem** — sem eles, a calibração self-paced é fraca.
- **Profundidade real só se prova com alunos reais** (este documento é arquitetura, não curso).

**18.3 Pergunta obrigatória: "O aluno autodidata consegue começar em 30 minutos?"**

A auditoria avalia, por perfil:

- **Caminho inicial claro?** Sim — Seção 0 "Comece aqui" por perfil.
- **Primeiro comando?** Sim — `make setup` / `make test` / `make check` (nada de versão futura).
- **Primeiro artefato?** Sim — `problem-framing.md` ou `capstone-summary.md` (template).
- **Primeira evidência?** Sim — repo público + `progress.md` iniciado (ou setup verde / CI verde).
- **Modo low-cost?** Princípio definido; **valores a preencher** (backlog, prioridade alta).
- **Troubleshooting?** Padrão definido (satélite por módulo); **conteúdo a criar** (backlog, prioridade alta).
- **Referência sem mentor?** Reference solutions/exemplos definidos; **a criar** (backlog, prioridade alta).

> **Veredito.** O **caminho** de 30 minutos está desenhado e é honesto; a **experiência completa** depende de três itens de backlog de prioridade alta (custos, troubleshooting, reference solutions). Até criá-los, o self-study funciona com o starter + self-assessment + bloqueadores, mas **a calibração fica parcial** — e isso deve ser declarado ao aluno.

**18.4 O que validar na 1ª cohort.** Tempo real por nível vs study plans; clareza dos checkpoints; se os bloqueadores pegam o que deveriam; se a defesa técnica discrimina maturidade.

**18.5 O que validar com autodidatas.** Se conseguem começar em 30 minutos sozinhos; se o self-assessment + exemplos bastam para calibrar; onde travam sem mentor; se o low-cost mode segura o custo.

**18.6 O que NÃO devemos construir ainda.** Trilhas avançadas · formação de SWE detalhada · LMS/plataforma · badges/certificados · estrutura de repositório real · valores de custo cravados. Primeiro: validar o core com gente real.

---

*Fim do documento canônico — Formação Polaris em Applied AI Engineering, draft v0.1.*
