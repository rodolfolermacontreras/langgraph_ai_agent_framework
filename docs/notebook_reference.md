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
