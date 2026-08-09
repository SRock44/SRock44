<!--
  GitHub Profile README: Sean (SRock44), terminal / monospace
  Repo must be named exactly: SRock44/SRock44
  Design system: bg #0d1117 · accent #00d4ff (cyan) · accent #7928ca (purple)
  · muted #8b949e · plain text over badges, code blocks as the primary unit
-->

<!-- ░░░ HEADER ░░░ -->
<div align="center">

# Sean

</div>

```
guest@github:~$ whoami
sean · CS @ NYIT (class of 2026) · Lab Consultant @ NYIT ETIC

guest@github:~$ cat interests.txt
AI/ML in production - models that retrain themselves, get monitored, and ship.
```

<!-- ░░░ ABOUT ░░░ -->
## About

I'm a computer science student at **NYIT** (graduating 2026), currently working as a **Laboratory Consultant** at the NYIT ETIC Lab. I work across the stack but I'm most drawn to **AI/ML in production**: models that retrain themselves, get monitored, and actually ship.

- I run a production ML pipeline that predicts NBA/MLB game winners and player props with an XGBoost + LightGBM ensemble: test-set accuracy, 50+ engineered features, and a fully automated Celery/Optuna retraining loop with MLflow-tracked champion/challenger promotion, running on a self-hosted GPU server. The feature engineering and model training code is open-sourced at **[sports-prediction-model](https://github.com/SRock44/sports-prediction-model)**.
- I built **[rmbr](https://github.com/SRock44/rmbr)**, an embedded, local-first memory + retrieval engine for AI agents: one SQLite file, no server, no API key required. Published on PyPI, listed as an MCP server on the [official MCP registry](https://registry.modelcontextprotocol.io) and on [Glama.ai](https://glama.ai/mcp/servers/SRock44/rmbr), with an optional HTTP mode too.
- I built **[pyhomerun](https://github.com/SRock44/pyhomerun)**, a zero-dependency Python library for baseball stats: sabermetrics and an MLB Stats API client, published on PyPI.
- On the side, I develop custom **Lua** scripts for games like *Holdfast*, *GTA*, and *FiveM*, which is where I learned to read messy systems, reverse-engineer APIs, and ship for real players.
- I built **[SoundKitten](https://soundkitten.org)**, a lightweight Rust/Tauri desktop SoundCloud client for people who'd rather not run a browser wrapped in an "app." Source at **[soundkitten](https://github.com/srock44/soundkitten)**.

<!-- ░░░ TECH STACK ░░░ -->
## Tech Stack

```
guest@github:~$ cat stack.txt
Languages    Python · TypeScript · JavaScript · Lua
ML / Data    PyTorch · Pandas · XGBoost
Tools        Node.js · Git
```

<!-- ░░░ FEATURED PROJECTS ░░░ -->
## Featured Projects

### rmbr

An embedded, local-first memory + retrieval engine for AI agents: one SQLite file, no server, no API key.

```
$ pip install rmbr
```

`Python` `SQLite` `MCP` &nbsp;·&nbsp; [source](https://github.com/SRock44/rmbr) · [PyPI](https://pypi.org/project/rmbr/) · [MCP registry](https://registry.modelcontextprotocol.io) · [Glama](https://glama.ai/mcp/servers/SRock44/rmbr)

### SoundKitten

A lightweight Rust/Tauri desktop SoundCloud client for people who'd rather not run a browser wrapped in an "app."

```
$ open soundkitten.org
```

`Rust` `Tauri` `Desktop` &nbsp;·&nbsp; [source](https://github.com/srock44/soundkitten) · [site](https://soundkitten.org)

### pyhomerun

A clean, dependency-free Python library for baseball stats: sabermetrics + an MLB Stats API client.

```
$ pip install pyhomerun
```

`Python` `Sabermetrics` `Zero Deps` &nbsp;·&nbsp; [source](https://github.com/SRock44/pyhomerun) · [PyPI](https://pypi.org/project/pyhomerun/)

### sports-prediction-model

Open-source feature engineering + XGBoost/LightGBM training code powering my production NBA/MLB winner & player-prop models. Self-retrains nightly via Celery + Optuna, MLflow-tracked.

```
$ git clone https://github.com/SRock44/sports-prediction-model
```

`Python` `XGBoost` `MLOps` &nbsp;·&nbsp; [source](https://github.com/SRock44/sports-prediction-model)

<!-- ░░░ DEV METRICS ░░░ -->
## Dev Metrics

<!--START_SECTION:waka-->
Populated by the `Dev Metrics` GitHub Action on its next scheduled run (or trigger it manually from the Actions tab).
<!--END_SECTION:waka-->

<!-- ░░░ CONNECT ░░░ -->
## Connect

```
guest@github:~$ echo $CONTACT
email:     sean@rockwitz.com
github:    github.com/SRock44
linkedin:  linkedin.com/in/srockwitz

# open to internships & new-grad roles
```
