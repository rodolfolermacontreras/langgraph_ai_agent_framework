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

Knowledge Base Agents & Reliability

- **Goal:** Build agents that use a knowledge base (KB) for accurate, up-to-date answers while remaining resilient to missing or stale data.
- **Design patterns:** Retrieval-Augmented Generation (RAG) with separation between retrieval and generation; retrieval scoring + reranking; fallback to safe responses when confidence is low.
- **KB preparation:** Chunk documents (512–2,048 tokens), include metadata (source, date, type), and normalize text (cleaning, de-duplication).
- **Embeddings & vector store:** Choose embeddings that match your domain; store vectors with metadata and use vector stores that support metadata filtering and efficient nearest-neighbor search.
- **Retrieval quality:** Use hybrid retrieval (BM25 + embeddings) for better recall; rerank top-k candidates using a cross-encoder or re-ranker.
- **Freshness & updates:** Implement an ingestion pipeline with incremental updates, content versioning, and last-updated timestamps. Add TTL or periodic re-embedding for frequently changing content.
- **Context windows & chunking:** Limit retrieved context by token budget; prefer smaller, relevant chunks with overlap; add provenance snippets for transparency.
- **Safety & hallucination mitigation:** Add explicit grounding prompts, include provenance citations in responses, and validate generated statements against retrieved sources when possible.
- **Caching & latency:** Cache retrieval results for repeated queries, use async loaders for large ingestion, and add circuit-breaker logic for downstream timeouts.
- **Observability & diagnostics:** Log retrieval traces, model token usage, latencies, and a retrieval confidence score. Capture diagnostic strings from the LLM SDK for failed/slow calls.
- **Testing & metrics:** Track end-to-end metrics: MRR/Recall@k for retrieval, factuality score, user-facing accuracy, latency, and cost (tokens/RUs). Build unit tests for ingestion and integration tests for end-to-end RAG flows.
- **Deployment & secrets:** Keep Foundry/API keys in `.env` (or CI secrets). Use rate-limit retries and region preferences, and enforce least-privilege access for KB stores.
- **Next steps (playground):**
  - Create a `playground/03_rag_kb.ipynb` that ingests a small sample KB, builds embeddings, runs retrieval, and shows provenance in responses.
  - Add a test harness in `scripts/` to validate retrieval quality after each KB update.

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

Flow Diagram (what's next)

Below is a visual flow of the recommended next steps. You can paste this Mermaid diagram into a renderer (VS Code Mermaid preview, GitHub, or other tools) to view it graphically.

```mermaid
flowchart TD
  A[Start: Run playground notebooks] --> B{Comfortable with Stages 0-2?}
  B -- No --> C[Repeat: Stage 0-2 exercises]
  B -- Yes --> D[Choose next focused notebook]
  D --> D1[RAG: Retrieval-Augmented Generation]
  D --> D2[Text2SQL: Structured queries from text]
  D --> D3[LangGraph Pipeline: nodes + checkpoints]
  D1 --> E[Test RAG with in-memory vector store]
  D2 --> E2[Build Text2SQL using sample DB & minimal SQL executor]
  D3 --> E3[Wire a small LangGraph workflow for Text2SQL]
  E --> F[Iterate: add real APIs (Foundry) behind env guard]
  E2 --> F
  E3 --> F
  F --> G[Prepare for production: secrets, retries, monitoring]
  G --> H[Done]
```

Note about `.env` loader and missing file

- If a notebook prints: `No .env file found at C:\\Training\\Udacity\\AI_Agents_LangGraph\\playground\\.env`, that means the loader attempted to read a `.env` file in the current working directory (the `playground/` folder) and didn't find one. The loader in `playground/01_basics_overview.ipynb` looks for a `.env` file at the notebook's working directory by default.
- Recommended: create the `.env` file at the project root (C:\\Training\\Udacity\\AI_Agents_LangGraph\\.env) rather than inside `playground/`. The loader will read that file when notebooks are executed from the project root or when you pass the full path to the loader.

Quick example to create a safe local `.env` at the project root (PowerShell):

```powershell
# Run from project root
echo "FOUNDRY_PROJECT_ENDPOINT=https://your-foundry.example" > .env
echo "FOUNDRY_PROJECT_REGION=westus" >> .env
echo "FOUNDRY_DEPLOYMENT_NAME=gpt-4.1" >> .env
echo "FOUNDRY_API_KEY=replace-with-your-key" >> .env
```

If you prefer the loader to read from a specific path inside a notebook, call it with the absolute path, for example:

```python
# In a notebook cell
from pathlib import Path
from playground import load_dotenv_if_present  # if you refactor loader into a module
load_dotenv_if_present(dotenv_path=Path('..') / '.env')
```

I will now commit and push this update to `docs/roadmap.md`.

## Execution Log (recent changes and results)

Summary of what was evaluated and why:
- Evaluated: `playground/01_basics_overview.ipynb` and `playground/02_code_examples.ipynb` to ensure they run end-to-end in the project's local virtual environment (`.venv`).
- Why: The `01` notebook couldn't find a `.env` when executed from inside `playground/`. This blocks running examples that conditionally enable Foundry calls.

What I changed and why:
- Updated the `.env` loader inside `playground/01_basics_overview.ipynb` to search upward up to 5 parent directories for a `.env` file (function: `find_upwards`).
  - Reason: Notebooks are often executed with different working directories; searching upwards makes the loader robust while still keeping secrets local.
- Added `run_notebooks.py` (temporary runner) to execute notebooks headlessly using `nbclient` and set Windows selector event-loop policy to avoid zmq Proactor issues during headless execution.
  - Reason: `nbconvert` produced nested output path issues on Windows; `nbclient` provides a reliable programmatic runner.
  - Note: `run_notebooks.py` is scaffolding used to validate notebooks and should be reviewed and removed later once CI or a standardized test runner is in place.
- Updated `README.md` with the current directory tree and a short action plan (so the team has a single source of truth about structure and next steps).

Results from running the notebooks in `.venv`:
- Executed copies were produced and saved as:
  - `playground/01_basics_overview.executed.ipynb` (success)
  - `playground/02_code_examples.executed.ipynb` (success)
- During execution there was a transient zmq warning/assertion logged related to the Windows Proactor event loop; this did not prevent notebook execution but we set the selector event loop policy in `run_notebooks.py` to reduce this noise.

Files changed / committed as part of this iteration:
- `playground/01_basics_overview.ipynb` — loader and memory improvements
- `playground/02_code_examples.ipynb` — made self-contained and runnable
- `playground/01_basics_overview.executed.ipynb` — executed artifact
- `playground/02_code_examples.executed.ipynb` — executed artifact
- `run_notebooks.py` — temporary runner (scaffolding)
- `README.md` — updated directory tree and short plan
- `docs/roadmap.md` — (this file) updated with flow diagram and the execution log

Next recommended steps (short):
- Confirm where you keep `.env` (project root recommended) and **do not commit** it. Update notebooks to call `load_dotenv_if_present()` with a specific path if you prefer a different layout.
- Decide which focused playground notebook to create next (RAG recommended). I can draft it and make it self-contained with toggles to enable Foundry calls.
- Plan to move `run_notebooks.py` into a small `scripts/` test harness or delete it after CI is set up.

Change rationale notes (why we changed code):
- Robustness: Searching upwards for `.env` reduces false negatives when running notebooks from nested folders.
- Reproducibility: Executed notebook artifacts help verify examples run in the target environment and make debugging easier.
- Traceability: Recording the execution log and reasons for change helps review and rollback if needed.
