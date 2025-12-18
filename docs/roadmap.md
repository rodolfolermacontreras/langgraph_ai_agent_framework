# Roadmap: Learn to Build AI Agents with LangGraph

This roadmap is tailored for data scientists who know Python for analysis and want a structured path to learn agent development with LangChain/LangGraph.

Stage 0 — Foundations (1-2 days)
- Goal: Understand LLM basics, prompt structure, and simple programmatic calls.
- Tasks:
  - Read `playground/01_basics_overview.ipynb` and run the examples.
  - Practice writing system/user prompts and few-shot prompts.

Stage 1 — Simple Agents & Tools (2-3 days)
- Goal: Learn tool patterns and simple agent loops.
- Tasks:
  - Read `playground/02_code_examples.ipynb`.
  - Implement local tool stubs and rule-based dispatch.
  - Add a `Memory` class and persist short-term context.

Stage 2 — LangChain Basics (3-4 days)
- Goal: Learn LangChain Chat primitives and prompt templates.
- Tasks:
  - Work through `notebooks/L2_demo_01_langchain_101.ipynb`.
  - Practice prompt templates, few-shot, and ChatOpenAI wrapper usage.

Stage 3 — Tool Calling & ReAct (4-6 days)
- Goal: Enable function/tool calling and ReAct patterns.
- Tasks:
  - Study `notebooks/L1_demo_02_function_calling.ipynb`, `L1_demo_03_react.ipynb`, and `L1_solution_exercise_04_tool_calling.ipynb`.
  - Build tools that can be called by the model and handle their outputs safely.

Stage 4 — LangGraph Workflows (4-6 days)
- Goal: Build resilient workflows with nodes, reducers, and checkpoints.
- Tasks:
  - Read `notebooks/L3_demo_01_langgraph_workflow.ipynb` through `L3_demo_08_checkpoints.ipynb`.
  - Implement a small LangGraph pipeline that runs a Text2SQL flow or a RAG flow.

Stage 5 — Retrieval, Embeddings, and RAG (3-5 days)
- Goal: Use embeddings and vector stores for contextual retrieval.
- Tasks:
  - Study `notebooks/L2_demo_05_RAG.ipynb`.
  - Build an embeddings + retriever demo using local in-memory store.

Stage 6 — Production Readiness & Tooling (ongoing)
- Topics:
  - Observability, diagnostics, retry logic, rate-limiting (handle 429), and costs (RUs / tokens).
  - Secure secret management, APIs, and environment isolation.

Tips for Learning:
- Keep small, reproducible examples in `playground/`.
- Use `.env` files locally but never commit them. `.gitignore` is set up.
- Start with stubbed tools before wiring real external APIs.
- Ask for one small, guided project to build from scratch (I can propose one).

Roadmap next-step: Create focused notebooks for `RAG`, `Text2SQL`, and `LangGraph` examples in `playground/` once you're comfortable with Stages 0–2.

Foundry (Microsoft Foundry) setup and local `.env` usage
- Create a local `.env` file in the project root with the following keys (do NOT commit this file):
  - `FOUNDRY_PROJECT_ENDPOINT` — the project endpoint URL
  - `FOUNDRY_PROJECT_REGION` — the region (e.g., `westus`)
  - `FOUNDRY_DEPLOYMENT_NAME` — deployment name (e.g., `gpt-4.1`)
  - `FOUNDRY_API_KEY` — your secret project API key

- Example workflow in notebooks:
  1. Install `python-dotenv` in your local environment: `pip install python-dotenv`.
  2. Load env vars in a notebook using `from dotenv import load_dotenv; load_dotenv()`.
  3. Read values from `os.environ` and configure your client SDK with the foundry endpoint, deployment name, and key.

- Security notes:
  - Keep `.env` out of version control and never paste secrets into shared notebooks.
  - Use `FOUNDRY_API_KEY` only from secure environments or CI secrets when deploying.
