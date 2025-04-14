
# 🧠 ADK-Free Multi-Agent Design System

This project is a fully refactored, dependency-free version of a multi-agent software design assistant.
It replaces Google ADK + LiteLLM with pure Python, and supports OpenAI or Ollama LLMs.

---

## 🚀 Features

- ✅ Modular agents: Requirements → System Design → Module Plan
- ✅ Shared `state` flow between agents
- ✅ CLI-first: No web UI, simple command line execution
- ✅ Logging with `logger`
- ✅ `pytest` test coverage
- ✅ Supports OpenAI or local Ollama backend

---

## 📁 Project Structure

```
adk_multi_agent_project/
├── agents/
│   ├── requirement_agent/
│   ├── system_design_agent/
│   └── module_design_agent/
├── core/
│   ├── base_agent.py
│   ├── llm_api.py
│   └── config.py
├── workflows/
│   └── design_pipeline.py
├── tests/
│   └── test_agents.py
└── run.py
```

---

## 📦 Installation

```bash
git clone <this_repo>
cd adk_multi_agent_project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Required Environment
```bash
OPENAI_API_KEY=sk-xxxx
USE_MODEL=openai   # or ollama
OLLAMA_BASE=http://localhost:11434
```

---

## 🔁 Run with Docker

```bash
docker build -t multi-agent .
docker run --rm -it \
  -e OPENAI_API_KEY=sk-xxxx \
  -e USE_MODEL=openai \
  multi-agent
```

> 💡 For Ollama:
> ```bash
> docker run --rm -it \
>   -e USE_MODEL=ollama \
>   -e OLLAMA_BASE=http://host.docker.internal:11434 \
>   multi-agent
> ```

---

## 🧪 Run the System
```bash
python run.py
```

## 🧪 Tests
```bash
pytest tests/
```

---

## ✅ TODO Suggestions
- [ ] Add agent streaming output
- [ ] Add evaluation layer (e.g. LLM-assisted self-checks)
- [ ] Wrap with FastAPI or Gradio UI

---

## 💡 License
MIT (or as you choose)
