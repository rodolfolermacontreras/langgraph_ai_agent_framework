## Learning Path: Build Practical AI Agents with LangChain & LangGraph

This learning path is organized into staged milestones to take you from LLM basics to production-ready agent architecture. Each stage lists target notebooks, hands-on exercises, and suggested deliverables.

Stage 0 — Foundations (1-2 days)
- Goal: Understand LLM calls, prompt structure, and simple memory.
- Notebooks: `notebooks/L1_starter_exercise_01_simple_llm_calls.ipynb`, `notebooks/L1_demo_01_memory_layer.ipynb`
- Exercises: run examples, vary prompts, implement a tiny `Memory` class that stores last N messages.
- Deliverable: short report with 3 prompt experiments and results.

Stage 1 — Tools & Agent Patterns (2-4 days)
- Goal: Learn tools, function-calling, and ReAct loops.
- Notebooks: `notebooks/L1_demo_02_function_calling.ipynb`, `notebooks/L1_demo_03_react.ipynb`, `notebooks/L1_solution_exercise_04_tool_calling.ipynb`
- Exercises: implement a stub tool, wire it into a ReAct loop, and log tool calls.
- Deliverable: runnable notebook demonstrating tool calls and a short explanation of when to use tools vs retrieval.

Stage 2 — LangChain Primitives & Chaining (3-4 days)
- Goal: Learn LangChain prompt templates, chat wrappers, and LCEL.
- Notebooks: `notebooks/L2_demo_01_langchain_101.ipynb`, `notebooks/L2_demo_04_LCEL.ipynb`, `notebooks/L2_demo_06_tools.ipynb`
- Exercises: build a small chain that takes user intent → generates steps → executes a summarizer.
- Deliverable: chain notebook and a one-paragraph explanation of prompt/template choices.

Stage 3 — LangGraph Workflows & Checkpoints (4-6 days)
- Goal: Build robust workflows with nodes, state, and checkpoints.
- Notebooks: `notebooks/L3_demo_01_langgraph_workflow.ipynb`, `notebooks/L3_demo_03_reducers.ipynb`, `notebooks/L3_demo_08_checkpoints.ipynb`
- Exercises: create a small StateGraph with an LLM node and a reducer that summarizes messages; add a `MemorySaver` checkpoint and replay a thread.
- Deliverable: LangGraph workflow notebook and short video or GIF showing replay.

Stage 4 — Retrieval, Embeddings & RAG (4-7 days)
- Goal: Build RAG pipelines with vector stores and provenance.
- Notebooks: `notebooks/L2_demo_05_RAG.ipynb`, `notebooks/L4_demo_03_embeddings.ipynb`, `notebooks/L4_demo_04_chromadb.ipynb`, `notebooks/L4_solution_exercise_01_kb_agent.ipynb`
- Exercises: ingest a sample PDF, chunk, embed, and run retrieval-augmented Q&A with provenance snippets.
- Deliverable: `playground/03_rag_kb.ipynb` expanded into a production-like mini-demo.

Stage 5 — Agentic Decisions & HITL (3-5 days)
- Goal: Add decision-making to RAG workflows and human approvals.
- Notebooks: `notebooks/L4_demo_05_agentic_rag.ipynb`, `notebooks/L4_demo_07_human_in_the_loop.ipynb`
- Exercises: build an evaluator node that triggers web research if retrieval confidence is low; add a breakpoint for human approval before external calls.
- Deliverable: LangGraph workflow with evaluator and HITL checkpoint.

Stage 6 — Long-Term Memory & LangMem (2-4 days)
- Goal: Enable persistent memory and user preference recall.
- Notebooks: `notebooks/L4_demo_06_langmem.ipynb`, `notebooks/L3_demo_05_database_toolkit.ipynb`
- Exercises: wire a memory tool into an agent, store user preferences, and retrieve across sessions.
- Deliverable: a small demo showing setting and retrieving preferences across separate runs.

Stage 7 — Evaluation, Observability & Reliability (ongoing)
- Goal: Establish metrics, MLflow tracing, and RAGAS evaluation.
- Notebooks: `notebooks/L4_demo_09_evaluation.ipynb`, `notebooks/L4_demo_08_mlflow_observability.ipynb`
- Exercises: run RAGAS on small datasets, capture MLflow runs, and log metrics like recall@k and faithfulness.
- Deliverable: evaluation notebook and MLflow experiment showing tracked runs.

Stage 8 — Production Readiness & Security (ongoing)
- Goal: Deployable architecture patterns, secrets, and security hygiene.
- Notebooks: `notebooks/L4_demo_10_security_deployment.ipynb`, `notebooks/L3_demo_05_database_toolkit.ipynb`
- Exercises: add retry logic, rate-limit handling, and ensure secrets use `.env`/CI secrets; run a security checklist.
- Deliverable: a short architecture diagram and a deployment checklist.

How I’ll help next
- I can auto-generate small exercises and scaffold notebooks for each Stage.
- I can create `scripts/update_notebook_reference.py` to auto-sync `docs/notebook_reference.md` from notebook metadata.
- I can add a lightweight GitHub Actions workflow to run `scripts/run_notebooks.py` or the notebook tests on push.

Would you like me to:
- A) Create `docs/learning_path.md` (done) and commit it (next), or
- B) Immediately scaffold the exercise notebooks for Stage 4 (RAG) now?
