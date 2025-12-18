# Notebook Reference and Contents

This document summarizes the purpose, tools, and topics covered in each notebook in the project. Use this as a reference to quickly locate examples and explanations for specific concepts.

---

## L1_demo_01_memory_layer.ipynb
**Purpose:** Demonstrates building conversational memory with OpenAI API, tracking user and assistant messages.
**Tools/Libraries:** openai, dotenv, Python typing
**Topics:** OpenAI client, message memory, chat function, class-based memory, conversation history

---

## L1_starter_exercise_01_simple_llm_calls.ipynb
**Purpose:** Hands-on intro to basic LLM calls using OpenAI SDK, focusing on parameters and prompt engineering.
**Tools/Libraries:** openai
**Topics:** OpenAI client, model/temperature, system prompts, reusable LLM call function, prompt experimentation

---

## L2_demo_01_langchain_101.ipynb
**Purpose:** Introduces LangChain basics: chat structure, prompt templates, few-shot learning.
**Tools/Libraries:** langchain_openai, langchain_core, dotenv
**Topics:** ChatOpenAI, System/Human/AI messages, prompt engineering, PromptTemplate, FewShotPromptTemplate

---

## L1_solution_exercise_04_tool_calling.ipynb
**Purpose:** Shows how to enable tool-calling in an agent, allowing dynamic invocation of external functions by the LLM.
**Tools/Libraries:** openai, dotenv, requests, datetime, inspect, typing, json
**Topics:** Memory class, tool registration, Tool abstraction, Agent class, tool execution, recursive tool calls

---

## L1_demo_02_function_calling.ipynb
**Purpose:** Demonstrates function/tool calling with OpenAI, including memory and tool call tracking.
**Tools/Libraries:** openai, dotenv, typing, json
**Topics:** Memory class, chat_with_tools function, tool schema, tool call tracking, manual tool execution

---

## L1_demo_03_react.ipynb
**Purpose:** Implements the ReAct pattern for agents, enabling reasoning and acting via tool calls.
**Tools/Libraries:** openai, dotenv, typing, inspect, json
**Topics:** Tool abstraction, StopReactLoopException, Agent class with ReAct loop, tool registration, multi-step reasoning

---

## L1_demo_04_multi_agents.ipynb
**Purpose:** Demonstrates multi-agent collaboration, including peer agent calls and message passing.
**Tools/Libraries:** openai, dotenv, typing, inspect, json
**Topics:** Agent class with peer agents, call_peer_agent tool, agent memory, multi-agent task delegation

---

## L1_solution_exercise_02_agents_from_scratch.ipynb
**Purpose:** Guides building a simple AI Agent from scratch, focusing on role, instructions, and response structure.
**Tools/Libraries:** openai, dotenv
**Topics:** Agent class, system prompt, invoke method, role/instructions, configurable parameters

---

## L1_solution_exercise_03_self_reflection.ipynb
**Purpose:** Adds self-reflection and memory to agents, enabling iterative critique and response refinement.
**Tools/Libraries:** openai, dotenv, typing, json
**Topics:** Memory class, self-reflection prompt, Agent class with critique, iterative refinement, logging

---

## L2_demo_02_streaming.ipynb
**Purpose:** Demonstrates streaming LLM responses, chunking, and resuming interrupted streams.
**Tools/Libraries:** langchain_openai, langchain_core, dotenv
**Topics:** Streaming, chunking, resume, ChatBot class, async invoke, event handling

---

## L2_demo_04_LCEL.ipynb
**Purpose:** Introduces LangChain Expression Language (LCEL) for chaining, composing, and parallelizing LLM calls.
**Tools/Libraries:** langchain_openai, langchain_core, dotenv
**Topics:** PromptTemplate, StrOutputParser, RunnableSequence, RunnableLambda, RunnableParallel, batch/stream/invoke

---

## L2_demo_05_RAG.ipynb
**Purpose:** Demonstrates Retrieval-Augmented Generation (RAG) with Wikipedia, embeddings, and vector stores.
**Tools/Libraries:** langchain_openai, langchain_core, langchain_community, langchain_text_splitters, dotenv
**Topics:** WikipediaLoader, RecursiveCharacterTextSplitter, OpenAIEmbeddings, InMemoryVectorStore, retriever, RAG chain

---

## L2_demo_06_tools.ipynb
**Purpose:** Demonstrates how to create, bind, and use custom tools with LangChain and OpenAI LLMs, including tool invocation and result handling.
**Tools/Libraries:** langchain_openai, langchain_core, langchain.tools, dotenv
**Topics:** Tool creation, tool binding, tool calls, message handling, OpenAI function calling, tool result feedback loop.

---

## L2_demo_07_agent.ipynb
**Purpose:** Shows how to build a simple agent class that can use tools, maintain memory, and interact with users using LangChain and OpenAI.
**Tools/Libraries:** langchain_openai, langchain_core, langchain.tools, dotenv
**Topics:** Agent class design, tool integration, memory management, tool call parsing, agent invocation pattern.

---

## L2_solution_exercise_01_chatbot_application.ipynb
**Purpose:** Solution notebook for building a customizable chatbot with memory, few-shot prompting, and role/personality control.
**Tools/Libraries:** langchain_openai, langchain_core, dotenv
**Topics:** Chatbot class, few-shot prompting, memory, role customization, conversation flow, personality engineering.

---

## L2_solution_exercise_02_multi_step_workflow.ipynb
**Purpose:** Solution notebook for building a multi-step AI workflow using LCEL, including idea generation, analysis, and report formatting.
**Tools/Libraries:** langchain_openai, langchain_core, pydantic
**Topics:** Multi-step chains, prompt templates, output parsing, business idea generation, analysis, report structuring, end-to-end chaining.

---

## L3_demo_01_langgraph_workflow.ipynb
**Purpose:** Introduces LangGraph workflows, showing sequential and LLM-based state graphs, node creation, and graph compilation.
**Tools/Libraries:** langgraph, langchain_openai, langchain_core, IPython.display
**Topics:** StateGraph, node/edge creation, sequential data processing, LLM node integration, graph visualization.

---

## L3_demo_02_schemas.ipynb
**Purpose:** Explores schema design in LangGraph using TypedDict and Pydantic, and demonstrates state machines with conditional logic.
**Tools/Libraries:** langgraph, pydantic, typing_extensions, operator, IPython.display
**Topics:** TypedDict vs Pydantic, state machines, conditional edges, traffic light controller example, graph compilation.

---

## L3_demo_03_reducers.ipynb
**Purpose:** Demonstrates data processing in LangGraph using sequential, parallel, and reducer nodes, including message aggregation and LLM integration.
**Tools/Libraries:** langgraph, operator, langchain_openai, langchain_core, IPython.display
**Topics:** Sequential/parallel processing, reducers, message aggregation, custom state, LLM node with MessagesState.

---

## L3_demo_04_config.ipynb
**Purpose:** Shows how to use configuration and custom state in LangGraph nodes, including passing config to nodes and using RunnableConfig.
**Tools/Libraries:** langgraph, langchain_openai, langchain_core, IPython.display
**Topics:** Custom state, RunnableConfig, config passing, node parameterization, graph compilation.

---

## L3_demo_05_database_toolkit.ipynb
**Purpose:** Demonstrates building a database toolkit with SQLAlchemy and LangChain tools for table listing, schema inspection, and SQL execution.
**Tools/Libraries:** sqlalchemy, pandas, langchain_core, RunnableConfig
**Topics:** Database inspection, table schema, SQL execution, tool creation, toolkit pattern, SQLite integration.

---

## L3_demo_06_limiting_messages.ipynb
**Purpose:** Explores techniques for limiting, filtering, removing, and summarizing messages in LangGraph workflows.
**Tools/Libraries:** langgraph, langchain_openai, langchain_core, IPython.display
**Topics:** Message filtering, RemoveMessage, trim_messages, message summarization, token usage, workflow design.

---

## L3_demo_07_multiple_schemas.ipynb
**Purpose:** Demonstrates using multiple schemas and state transitions in LangGraph, including hidden layers and input/output state separation.
**Tools/Libraries:** langgraph, typing, IPython.display
**Topics:** Multiple schemas, hidden state, state transitions, input/output separation, workflow compilation.

---

## L3_demo_08_checkpoints.ipynb
**Purpose:** Shows how to use checkpoints in LangGraph workflows to track and restore state history for different threads.
**Tools/Libraries:** langgraph, langgraph.checkpoint.memory, IPython.display
**Topics:** Checkpoints, MemorySaver, state history, thread_id, workflow replay.

---

## L3_solution_exercise_01_router.ipynb
**Purpose:** Solution notebook for building a LangGraph router that dynamically routes input to different nodes based on user action.
**Tools/Libraries:** langgraph, typing, IPython.display
**Topics:** Conditional edges, routing function, node logic, error handling, workflow compilation.

---

## L3_solution_exercise_02_text2sql.ipynb
**Purpose:** Solution notebook for building a Text2SQL agent that converts natural language to SQL, executes queries, and returns results.
**Tools/Libraries:** langchain_openai, langgraph, sqlalchemy, sql_toolkit, IPython.display
**Topics:** Text2SQL, tool integration, SQL execution, MessagesState, workflow design, user query parsing.

---

## L3_solution_exercise_03_loan_agent.ipynb
**Purpose:** Solution notebook for building a LangGraph workflow for a loan negotiation agent, including tools, negotiation status, and checkpoints.
**Tools/Libraries:** langchain_openai, langgraph, langchain_core, langgraph.checkpoint.memory, ToolNode, IPython.display
**Topics:** Loan agent, negotiation workflow, tool calls, status tracking, RemoveMessage, summarization, checkpoints, state history.

---

# Plan and Next Steps

- All notebook summaries are now consolidated in this single reference file.
- The docs/README.md file has been removed to comply with the single-README rule.
- Continue updating this file as new notebooks are added or existing ones are changed.
- Ensure all scripts and experiments are tracked and documented; remove or integrate scaffolding code as needed.
- Commit this update to version control as a major documentation refresh.

---

## L4_demo_01_persisting_memory.ipynb
**Purpose:** Demonstrates persisting conversational memory to a SQLite backend (SqliteSaver) so sessions can be resumed and audited.
**Tools/Libraries:** langgraph, langgraph.checkpoints (MemorySaver, SqliteSaver), sqlite3, Python stdlib
**Topics:** run_graph helper, StateGraph with MessageState, MemorySaver vs SqliteSaver, database schema (checkpoints, writes), metadata snapshots, thread_id-based session resumption, inspecting and querying `memory.db`.

---

## L4_demo_02_rag_pipelines.ipynb
**Purpose:** Explains Retrieval-Augmented Generation (RAG) pipelines end-to-end and demonstrates a sample e-commerce support use case.
**Tools/Libraries:** embeddings (Hugging Face / OpenAI), Chroma or in-memory vector store, text-splitter utilities, langchain-style loaders
**Topics:** retrieval → augmentation → generation flow, data collection and preprocessing, chunking and metadata, embedding generation, vector DB storage, example: retrieving return policy for electronics.

---

## L4_demo_03_embeddings.ipynb
**Purpose:** Builds intuition for embeddings generation, similarity search, and visualization (PCA) across providers (Hugging Face, OpenAI).
**Tools/Libraries:** sentence-transformers or OpenAI embeddings, numpy, scikit-learn (PCA), matplotlib
**Topics:** EmbeddingsFactory abstraction, embedding generation, semantic similarity (dot product), dimensionality reduction for visualization, provider trade-offs (dimension, quality, cost).

---

## L4_exercise_01_kb_agent_challenge.ipynb
**Purpose:** Hands-on challenge to build a Knowledge Base (KB) agent using RAG: load docs, vectorize, retrieve, and generate grounded answers with provenance.
**Tools/Libraries:** Chroma/FAISS, embedding provider, text splitter, LangGraph StateGraph, Chat LLM wrapper
**Topics:** document loading & vectorization, agent node retrieving context, augment + generate nodes, conditional routing, chunking, provenance and confidence thresholds.

---

## L4_demo_04_agentic_decisions_rag.ipynb
**Purpose:** Extends a RAG pipeline with agentic decision-making: evaluate retrieval quality and optionally trigger web research when retrieval is insufficient.
**Tools/Libraries:** LangGraph, retriever, small evaluator LLM chain, web search tool (tavily or similar)
**Topics:** retrieve → evaluator → (researcher | augment) → generate flow; routers to direct control flow; looping researcher node; cost/latency trade-offs for online search.

---

## L4_demo_05_langmem_longterm_memory.ipynb
**Purpose:** Demonstrates long-term memory via LangMem: persistent, vector-backed memory store for agent preferences and facts across sessions.
**Tools/Libraries:** langmem (OpenAIMemoryStore or equivalent), LangGraph, ReAct agent utilities
**Topics:** create_react_agent with memory store, manage_memory and search_memory tools, session examples (save preference, retrieve across sessions), tool-based memory management.

---

## L4_demo_06_reliability_observability.ipynb
**Purpose:** Introduces reliability concepts for AI agents: metrics, testing vs evaluation, observability basics, and operational concerns.
**Tools/Libraries:** logging, metrics libs (prometheus client examples), simple tracing utilities
**Topics:** accuracy/efficiency/cost KPIs, evaluation vs testing, logging & tracing, decision transparency, alerting, and suggested continuous evaluation loops.

---

## L4_demo_07_hitl_workflows.ipynb
**Purpose:** Implements Human-in-the-Loop (HITL) controls and breakpoints in LangGraph workflows for manual approval, edits, and supervised tool calls.
**Tools/Libraries:** LangGraph, input stubs for review, MessageState, MemorySaver for checkpointing during approvals
**Topics:** interrupt_before breakpoints, human approval flows (approve/abort/edit), resume with edited state, multi-step approval after tool calls, thread_id session handling.

---

## L4_demo_08_mlflow_observability.ipynb
**Purpose:** Integrates MLflow tracing and autologging into LangGraph workflows to capture runs, inputs/outputs, token usage, and artifacts.
**Tools/Libraries:** mlflow, mlflow.langchain.autolog (if available), LangGraph, local MLflow server examples
**Topics:** mlflow.set_tracking_uri, mlflow experiments/runs, autologging LLM inputs/outputs, node-level artifacts, run timelines, and visual inspection in MLflow UI.

---

## L4_demo_09_ragas_evaluation.ipynb
**Purpose:** Demonstrates evaluating RAG pipelines and agent workflows using RAGAS, producing objective metrics like faithfulness and context recall.
**Tools/Libraries:** RAGAS, LangGraph conversion utilities, evaluation dataset harness, optional judge model
**Topics:** constructing EvaluationDataset, metrics (LLMContextRecall, Faithfulness, FactualCorrectness), converting traces to RAGAS format, logging results.

---

## L4_demo_10_security_deployment.ipynb
**Purpose:** Covers security best practices for AI agent deployments: access control, prompt injection defenses, encryption, and incident response planning.
**Tools/Libraries:** examples with RBAC concepts, input sanitization snippets, monitoring hooks
**Topics:** data leakage mitigation, prompt input validation, RBAC & MFA recommendations, logging and incident response, balancing security and performance.

---

## L4 Knowledge Additions (User-provided summaries)

### Persisting Memory with a Database in LangGraph
**Summary:** Demonstrates saving conversation history to SQLite to persist session memory across restarts. Introduces a `run_graph` helper that invokes a `StateGraph` with a `thread_id` and shows two checkpointer configurations: `MemorySaver` (in-memory) and `SqliteSaver` (SQLite-backed). Explains inspecting `memory.db`, schema (`checkpoints`, `writes`), and retrieving serialized metadata (HumanMessage, AIMessage, model configs). Highlights benefits: resumable sessions, auditing, and searchability.

**Key steps:**
- `run_graph(query, graph, thread_id)` helper to invoke workflows.
- In-memory workflow using `MemorySaver` for ephemeral checkpoints.
- SQLite-persisted workflow using `SqliteSaver(db_path='memory.db')` for durable checkpoints.
- Inspect DB schema and `metadata` for step-by-step snapshots.

---

### RAG Pipelines: Enhancing Agents with Retrieval + Generation
**Summary:** Explains the RAG pattern: retrieval (embed query → vector DB search), augmentation (add retrieved docs to prompt), and generation (LLM answers using augmented context). Uses an e-commerce support example to show the difference between non-RAG and RAG responses, and covers preprocessing steps (collection, cleaning, chunking, embed, store).

**Notes:**
- Emphasizes chunking, metadata tagging, storage in vector DB (Chroma), and provider choices for embeddings.
- Discusses tradeoffs vs fine-tuning and recommends a combined approach: quick RAG prototyping, then selective fine-tuning for stable improvements.

---

### Embeddings in LangGraph Workflows
**Summary:** Introduces an `EmbeddingsFactory` to switch between Hugging Face and OpenAI embeddings. Demonstrates generating embeddings for sample sentences, computing similarities, and visualizing via PCA. Highlights provider tradeoffs (dimension, cost, and quality).

**Key steps:**
- Build embeddings with Hugging Face or OpenAI.
- Compute pairwise similarities using dot product.
- Use PCA for 2D visualization to inspect semantic clustering.

---

### Knowledge Base Agent Challenge (RAG exercise)
**Summary:** Exercise to assemble a KB agent: document loading, splitter (RecursiveCharacterTextSplitter), embedding + vector store, retrieve → augment → generate pipeline in a LangGraph `StateGraph`. Encourages learners to add provenance, chunk optimization, and conditional routing.

**Deliverables:**
- Vectorized KB collection and Chroma/FAISS-backed retrieval.
- Agent node that retrieves and generates grounded answers.
- Tests for retrieval quality and provenance display.

---

### Agentic Decisions in RAG Pipelines
**Summary:** Adds a decision layer that evaluates retrieved context quality and optionally triggers a live web search. Components: retriever, evaluator (LLM-based yes/no), researcher (web search tool), and routers to direct flow. Demonstrates dynamic, cost-aware control flow.

---

### Building Long-Term Memory with LangMem
**Summary:** Shows how to use `LangMem` (OpenAIMemoryStore or similar) to create persistent long-term memory. Demonstrates `create_react_agent` wired to memory tools (`manage_memory`, `search_memory`) and examples of storing and retrieving user preferences across sessions.

---

### Ensuring Reliability: Metrics, Testing, Observability
**Summary:** Covers reliability definitions and metrics (accuracy, efficiency, cost), differences between testing and evaluation, and observability practices (metrics, logs, tracing). Suggests continuous evaluation loops, alerting, and KPIs to keep agents reliable in production.

---

### Human-in-the-Loop (HITL) Approvals and Edits
**Summary:** Demonstrates breakpoints (`interrupt_before`) and manual approval/edit flows inside LangGraph workflows. Shows how to pause execution, solicit user approval or edits, and resume with updated state, enabling supervised tool calls and safer interaction.

---

### Observability with MLflow and LangGraph
**Summary:** Integrates MLflow for experiment tracking: set tracking URI, autolog LangChain events, and log node inputs/outputs and evaluation metrics. Demonstrates reviewing traces in MLflow UI and logging token usage/artifacts.

---

### Evaluating RAG and Agent Performance with RAGAS
**Summary:** Demonstrates converting LangGraph traces to RAGAS format and evaluating RAG pipelines with metrics like context recall, faithfulness, and factual correctness. Shows constructing `EvaluationDataset` and logging results (optionally to MLflow).

---

### Security Concerns in AI Agent Deployments
**Summary:** Discusses common threats (data leakage, prompt injection, unauthorized access) and recommends best practices: RBAC, MFA, input sanitization, logging, and incident response. Emphasizes ongoing monitoring and balancing security with usability.
