# LangGraph & LangChain Agent Playground

This project is a personal playground for exploring, creating, and experimenting with agentic workflows using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain).

## Project Structure (current)
- **.git/**: Git repository data
- **.venv/**: Local virtual environment (ignored by Git)
- **docs/**: Documentation files
	- notebook_reference.md
	- roadmap.md
- **notebooks/**: Original course notebooks and demos
- **playground/**: Small runnable notebooks for quick experiments
	- 01_basics_overview.ipynb
	- 02_code_examples.ipynb
- **scripts/**: Python scripts and utilities (scaffolding)
- **.env**: (local) environment file — DO NOT COMMIT secrets
- **.env.example**: Example environment file with placeholders
- **.gitignore**: Ignored files
- **README.md**: (this file)
- **Syllabus.pdf**: Course syllabus

## About This Repository
This repository is inspired by the Udacity course "Introduction to Agents with LangGraph." It is designed for hands-on learning and prototyping of agent logic, workflows, and integrations with LLMs.

### Key Concepts
- **Agents**: LLM-driven systems that dynamically control execution flow.
- **LangGraph**: Enables flexible, reliable, and visualizable agentic workflows using nodes (functions) and edges (routing logic).
- **LangChain**: Provides modular components for LLMs, tools, and memory, which can be orchestrated by LangGraph.

### Example Workflows
- Sequential data processing with state tracking
- LLM-powered Q&A and task routing
- Multi-node and multi-agent orchestration

Feel free to use, modify, and extend the notebooks and scripts as you learn!

## Current Action Plan (short)
- Validate `playground/` notebooks run in the local `.venv` and fix runtime issues.
- Create focused playground notebook (RAG) after validation.
- Keep documentation updated: record evaluations, test scripts, and reasons for code changes in `docs/`.

Notes:
- Always activate the virtual environment before installing packages or running notebooks:

```powershell
# From project root
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if present
```

- Do not commit `.env` or the `.venv` folder. Use `.env.example` for placeholders.

---

*Created and maintained for learning and experimentation. Notebooks and scripts may be rough or exploratory.*
