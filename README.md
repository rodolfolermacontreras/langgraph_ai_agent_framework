# LangGraph & LangChain Agent Playground

This project is a personal playground for exploring, creating, and experimenting with agentic workflows using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain).

## Project Structure (current)
- **.git/**: Git repository data
- **.venv/**: Local virtual environment (ignored by Git)
- **docs/**: Comprehensive documentation
- `roadmap.md`: Complete 6-stage learning roadmap with objectives, tasks, and mini-projects
- `notebook_reference.md`: Comprehensive guide to all notebooks with learning levels, time estimates, and prerequisites
- `learning_path.md`: Staged milestones from foundations to production-ready agents
- `session_memory.md`: Iteration log tracking major actions, decisions, and artifacts
- **notebooks/**: Original Udacity course notebooks (L1-L4 demos and exercises)
- **playground/**: Small runnable notebooks for quick experiments and learning
- `01_basics_overview.ipynb`: LLM fundamentals, message structure, prompt engineering, memory (enhanced with detailed explanations)
- `02_code_examples.ipynb`: Tools, agent loops, and tool routing patterns (enhanced with comprehensive examples)
- `03_rag_kb.ipynb`: Retrieval-Augmented Generation with vector search (7-step educational structure)
- **scripts/**: Python scripts and utilities (scaffolding)
- **.env**: (local) environment file  DO NOT COMMIT secrets
- **.env.example**: Example environment file with placeholders
- **.gitignore**: Ignored files (excludes `.venv`, `.env`, `*.executed.ipynb`)
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

## Current Status & Action Plan

### What's Ready Now
- [COMPLETE] **playground/01_basics_overview.ipynb**: Complete foundations guide (configuration, message structure, prompt engineering, memory)
- [COMPLETE] **playground/02_code_examples.ipynb**: Complete agent patterns guide (memory integration, tool creation, agent loops)
- [COMPLETE] **playground/03_rag_kb.ipynb**: Complete RAG implementation guide (7-step educational structure)
- [COMPLETE] **docs/roadmap.md**: Comprehensive 6-stage learning roadmap with objectives and mini-projects
- [COMPLETE] **docs/notebook_reference.md**: Complete reference guide to all notebooks with difficulty levels
- [COMPLETE] **docs/learning_path.md**: Staged milestones connecting notebooks to deliverables
- [COMPLETE] **docs/session_memory.md**: Detailed iteration log of all changes and decisions

### How to Get Started
1. Review the [docs/roadmap.md](docs/roadmap.md) to understand the learning progression
2. Start with [playground/01_basics_overview.ipynb](playground/01_basics_overview.ipynb) for LLM fundamentals
3. Progress to [playground/02_code_examples.ipynb](playground/02_code_examples.ipynb) for agent patterns
4. Move to [playground/03_rag_kb.ipynb](playground/03_rag_kb.ipynb) for RAG systems
5. Reference [docs/notebook_reference.md](docs/notebook_reference.md) for detailed guides to all course notebooks

Setup Instructions:
- Always activate the virtual environment before installing packages or running notebooks:

```powershell
# From project root
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if present
```

- Do not commit `.env` or the `.venv` folder. Use `.env.example` for placeholders.
- All playground notebooks include extensive inline comments, "What Just Happened?" explanations, and detailed exercises for self-directed learning.

---

## Documentation Overview

The docs folder contains comprehensive, interconnected guides:

- **[roadmap.md](docs/roadmap.md)**: Complete 6-stage learning roadmap (Foundations  Production)
  - Each stage has clear learning objectives, key concepts, and hands-on tasks
  - Estimated timeline: 4-6 weeks of focused, part-time study
  - Includes mini-projects and troubleshooting guides

- **[notebook_reference.md](docs/notebook_reference.md)**: Complete reference for ALL 40+ notebooks
  -  Beginner,  Intermediate,  Advanced difficulty ratings
  - Time estimates and prerequisite lists for each notebook
  - Multiple learning paths (Foundations  Production, Fast Track, RAG Specialist)
  - Topic index (memory, tools, RAG, evaluation, etc.)

- **[learning_path.md](docs/learning_path.md)**: Staged milestones connecting notebooks to deliverables
  - 8 stages from foundations through evaluation and reliability
  - Each stage lists target notebooks, exercises, and deliverables
  - Bridges theory (docs) with practice (notebooks)

- **[session_memory.md](docs/session_memory.md)**: Iteration log tracking all changes
  - Major actions, decisions, and artifacts
  - Why changes were made and how they fit the big picture
  - Helper code locations and rules for the virtual environment

---

## Playground Notebooks (Your Learning Base)

Three carefully enhanced notebooks for self-directed learning:

### 1. playground/01_basics_overview.ipynb
**Learn**: LLM fundamentals - configuration, messages, prompts, memory  
**Level**:  Beginner | **Time**: 30-45 minutes

What you'll understand:
- How to securely manage API keys with environment files
- The message structure all LLM APIs use (system, user, assistant roles)
- Prompt engineering principles and reusable templates
- Memory management to maintain conversation context

### 2. playground/02_code_examples.ipynb
**Learn**: Agent patterns - tools, routing, decision-making  
**Level**:  Beginner | **Time**: 45-60 minutes

What you'll understand:
- What distinguishes agents from simple LLM calls
- How to design tools with structured returns
- Agent loop patterns (observe  route  execute  respond)
- From keyword-based routing to LLM-powered decisions

### 3. playground/03_rag_kb.ipynb
**Learn**: Retrieval-Augmented Generation - embeddings, vectors, knowledge bases  
**Level**:  Beginner (teaches advanced concept) | **Time**: 60-90 minutes

What you'll understand:
- Why RAG solves the "hallucination" problem
- How embeddings turn text into searchable vectors
- Building knowledge bases and semantic search
- Integrating retrieval into agent workflows

---

*Created and maintained for learning and experimentation. Notebooks and scripts may be rough or exploratory.*
