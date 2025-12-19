# HealthBot Implementation Plan

**Project**: HealthBot: AI-Powered Patient Education System  
**Student**: Rodolfo Lerma  
**Course**: AI Agents with LangChain and LangGraph (Udacity)  
**Date**: 2025-12-19

---

## Executive Summary

This document outlines the implementation strategy for HealthBot, an AI-powered patient education chatbot that guides patients through medical topics using a structured conversation flow with comprehension checks.

---

## Project Structure

```
project/healthbot/
|-- src/                          # Core implementation
|   |-- workflow.py              # LangGraph workflow definition
|   |-- state.py                 # State schema and definitions
|   |-- nodes.py                 # Workflow node implementations
|   |-- tools.py                 # Tavily search and utility functions
|   |-- llm_config.py            # LLM client initialization (Azure Foundry)
|   |-- utils.py                 # Helper functions (display, input, validation)
|
|-- notebooks/                    # Jupyter notebooks
|   |-- 01_healthbot_main.ipynb  # Main execution notebook
|   |-- 02_testing.ipynb         # Testing and validation notebook
|
|-- config/                       # Configuration files
|   |-- env.example              # Example environment variables (NO SECRETS)
|   |-- settings.yaml            # Project settings and constants
|
|-- tests/                        # Test scripts (will be cleaned up after validation)
|   |-- test_workflow.py         # Unit tests for workflow
|   |-- test_nodes.py            # Unit tests for individual nodes
|
|-- reports/                      # Output reports
|   |-- healthbot_report.tex     # LaTeX report
|   |-- healthbot_report.pdf     # PDF version of report
|
|-- README.md                     # Project overview and instructions
```

---

## Implementation Phases

### Phase 1: Setup and Configuration
**Objective**: Establish secure credential management and project structure

**Tasks**:
1. Create config/env.example with placeholder variables
2. Create config/settings.yaml with workflow constants
3. Set up environment variable loading in Python (use .env pattern, NOT embedding keys)
4. Initialize .venv for this project (if not using existing workspace venv)
5. Verify all dependencies are available

**Deliverables**:
- Secure configuration system
- No hardcoded API keys anywhere
- Clear instructions for API key setup

**Why**: Professional security practices, easy configuration management

---

### Phase 2: Core Workflow Architecture
**Objective**: Design and implement the LangGraph workflow structure

**Tasks**:
1. Define State schema (MessagesState with additional fields):
   - messages: list of messages
   - health_topic: current topic
   - search_results: Tavily search results
   - summary: patient-friendly summary
   - quiz_question: generated question
   - patient_answer: user response
   - grade: assessment result
   - should_continue: loop control

2. Create LLM client initialization:
   - Use Azure Foundry endpoint (from existing .env)
   - NOT OpenAI (project uses Azure)
   - Initialize ChatOpenAI-compatible client

3. Design workflow nodes (8 core nodes):
   - ask_for_topic: Greet patient, ask for health topic
   - search_medical_info: Tavily search with medical focus
   - summarize_results: Create patient-friendly summary
   - present_summary: Display to patient, wait for readiness
   - generate_quiz: Create single comprehension question
   - present_quiz: Display question, get patient answer
   - evaluate_answer: Grade and provide feedback with citations
   - ask_continue: Ask if patient wants new topic or exit

4. Design edges and routing:
   - START -> ask_for_topic
   - ask_for_topic -> search_medical_info
   - search_medical_info -> summarize_results
   - summarize_results -> present_summary
   - present_summary -> generate_quiz
   - generate_quiz -> present_quiz
   - present_quiz -> evaluate_answer
   - evaluate_answer -> ask_continue
   - ask_continue -> [ask_for_topic (new topic) OR END (exit)]
   - Reset state when starting new topic

**Deliverables**:
- LangGraph workflow file with 8 nodes
- State schema definition
- Edge routing logic
- State reset mechanism

**Why**: Clear separation of concerns, reusable components, easy to test

---

### Phase 3: Node Implementation
**Objective**: Implement individual workflow nodes with proper error handling

**Node Details**:

**1. ask_for_topic (Patient Input)**
- Display greeting message
- Ask: "What health topic or medical condition would you like to learn about?"
- Return topic in state
- Error handling: validate non-empty input

**2. search_medical_info (Tavily Integration)**
- Use TavilySearchResults from langchain-community
- Query: "[health_topic] medical information patient education"
- Focus on reputable sources (medical journals, health organizations)
- Extract top N results
- Store raw results in state

**3. summarize_results (LLM Summarization)**
- Prompt LLM to create patient-friendly summary
- Include key points, treatment options, prevention tips
- Keep language simple (8th grade reading level)
- Include source citations in summary
- Store summary in state

**4. present_summary (Patient Review)**
- Display summary to patient
- Ask: "Have you finished reading? Type 'ready' to proceed to comprehension check"
- Wait for patient confirmation
- Validate input

**5. generate_quiz (LLM Evaluation)**
- Prompt LLM to create one relevant quiz question
- Question should test understanding of key points
- Question format: multiple choice or short answer
- Store question in state

**6. present_quiz (Patient Response)**
- Display quiz question
- Ask patient for their answer
- Store answer in state
- No validation (will evaluate next)

**7. evaluate_answer (Grading & Feedback)**
- Prompt LLM to grade the answer (1-100 scale)
- Provide explanation with citations from summary
- Format: "Grade: X/100. Explanation: [feedback with source citations]"
- Store grade and feedback

**8. ask_continue (Session Management)**
- Display grade and feedback
- Ask: "Would you like to learn about another topic? (yes/no)"
- Control state: should_continue = true/false
- If yes: state reset for next topic
- If no: exit workflow

**Deliverables**:
- nodes.py with all 8 node functions
- Error handling and input validation
- LLM prompt templates
- Tavily integration

**Why**: Modular design allows testing individual components

---

### Phase 4: Integration & Testing
**Objective**: Combine all components and verify functionality

**Tasks**:
1. Create main workflow.py combining all nodes
2. Add checkpointing for state management
3. Create 01_healthbot_main.ipynb for execution
4. Create 02_testing.ipynb for validation
5. Test each node individually
6. Run end-to-end workflow with sample inputs
7. Verify state resets properly between topics
8. Verify no data leakage between sessions

**Test Cases**:
- Valid topic (e.g., "diabetes")
- Multiple topics in sequence
- Answer evaluation accuracy
- State reset between sessions
- Edge cases (empty input, special characters)

**Deliverables**:
- Complete workflow.py
- Main execution notebook
- Testing notebook with results
- Test report documenting all test cases and results

**Why**: Ensures reliability before evaluation

---

### Phase 5: Evaluation & Validation
**Objective**: Assess HealthBot against project requirements

**Evaluation Criteria**:

1. Functionality Completeness
   - All 8 nodes implemented and working
   - Correct node sequence
   - Proper state management
   - Quiz grading accuracy

2. Patient Experience
   - Clear, easy-to-understand prompts
   - Non-medical language in summaries
   - Logical flow
   - Proper error handling

3. Information Quality
   - Medical accuracy (from reputable Tavily sources)
   - Appropriate reading level
   - Relevant quiz questions
   - Accurate grading with good explanations

4. Code Quality
   - No hardcoded secrets
   - Proper error handling
   - Clear variable names
   - Well-commented code
   - No orphan/temporary scripts

5. Documentation
   - README with setup instructions
   - Inline code comments
   - Workflow diagram
   - Evaluation report

**Success Metrics**:
- All nodes working without errors
- Successfully handles 3+ different health topics
- Quiz grading matches expert evaluation
- State properly reset between sessions
- All API keys secure (no leakage in code/notebooks)

**Deliverables**:
- Evaluation results spreadsheet
- Screenshots/logs of test runs
- Comparison against requirements checklist

**Why**: Validates that HealthBot meets all project objectives

---

### Phase 6: Reporting
**Objective**: Document the project implementation in a practical, concise report

**Report Contents** (8-12 pages - practical + complete):

1. **Title Page**
   - Project name
   - Student name
   - Course name
   - Date

2. **Executive Summary** (1 page)
   - Brief overview of what was built
   - Key achievements
   - How it solves the problem

3. **Problem & Solution** (1 page)
   - Patient education challenge
   - HealthBot solution approach
   - Expected benefits

4. **Architecture Overview** (2-3 pages)
   - Workflow diagram with node descriptions
   - State schema table
   - Technology stack
   - Data flow explanation

5. **Implementation Details** (3-4 pages)
   - The 8 nodes (one paragraph each with code snippets)
   - Azure Foundry LLM integration
   - Tavily search implementation
   - Session management approach

6. **Testing & Results** (2-3 pages)
   - Test cases executed
   - Sample conversation transcript
   - Grading accuracy verification
   - State reset validation
   - Screenshots/logs of test runs

7. **Key Learnings** (1 page)
   - Challenges encountered and solutions
   - Design decisions and rationale
   - What worked well
   - Future improvements

**Deliverables**:
- healthbot_report.tex (LaTeX source)
- healthbot_report.pdf (compiled PDF)
- All source code and configuration files

**Why**: Professional documentation for academic/portfolio purposes

---

### Phase 7: Cleanup & Final Commit
**Objective**: Ensure project is production-ready and well-documented

**Tasks**:
1. Delete test scripts (tests/ folder) - keep results only
2. Verify no API keys in any files
3. Update session_memory.md with complete work log
4. Create comprehensive README
5. Final git commit with theme message

**Cleanup Details**:
- Remove: test_*.py files (after saving results)
- Keep: Test results and validation reports
- Document: Why tests were removed, where to find results

**Deliverables**:
- Clean project folder
- Updated session_memory.md
- Professional README
- Final git commit

**Why**: Professional standards (no orphan scripts), easy for others to understand

---

## Technology Stack

**LLM**: Azure Foundry (gpt-4.1)
- Endpoint: FOUNDRY_PROJECT_ENDPOINT from .env
- Credentials: Already configured in workspace

**Search**: Tavily API
- Tavily key: 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 (user-provided)
- Will store in .env (not in code)

**Framework**: LangGraph + LangChain
- Workflow orchestration: LangGraph
- LLM integration: LangChain
- Community tools: langchain-community (Tavily integration)

**Environment**: Python .venv
- Virtual environment for this project
- All dependencies installed
- No global Python usage

**Notebooks**: Jupyter (.ipynb)
- Main execution
- Testing and validation
- Interactive patient simulation

---

## Key Design Decisions

1. **Azure Foundry instead of OpenAI**
   - Already configured in workspace
   - Meets all requirements
   - Cost-effective for learning

2. **Modular Node Architecture**
   - Each node is testable independently
   - Easy to debug
   - Clear separation of concerns

3. **State Schema** (instead of conversation chain)
   - Better tracking of workflow state
   - Supports complex branching
   - Enables proper session reset

4. **Patient-Friendly Language**
   - LLM-driven summarization ensures accessibility
   - Appropriate reading level
   - Maintains medical accuracy

5. **Citation-Based Grading**
   - Helps patient learn and verify
   - Improves trust in AI responses
   - Educational value

6. **Security-First Configuration**
   - All secrets in .env (not in code)
   - Config template provided
   - Easy for production migration

---

## Timeline

| Phase | Tasks | Estimated Time |
|-------|-------|-----------------|
| 1 | Setup & Configuration | 15 min |
| 2 | Workflow Architecture | 30 min |
| 3 | Node Implementation | 60 min |
| 4 | Integration & Testing | 45 min |
| 5 | Evaluation & Validation | 30 min |
| 6 | Reporting (practical, 8-12 pages) | 45 min |
| 7 | Cleanup & Commit | 15 min |
| **Total** | | **~3.5 hours** |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Tavily API quota exhaustion | Test with limited calls first, monitor usage |
| LLM generation quality | Prompt engineering and review of outputs |
| Patient input edge cases | Validation and error handling in each node |
| State management complexity | Careful schema design and thorough testing |
| Report generation complexity | Use established LaTeX templates and libraries |

---

## Success Criteria

[CHECKLIST]

- [x] Project structure created
- [ ] All 8 nodes implemented and functional
- [ ] Workflow tests pass (3+ different topics)
- [ ] No API keys in code/notebooks
- [ ] State properly resets between sessions
- [ ] LaTeX report generated (20-30 pages)
- [ ] PDF report created
- [ ] Final commit with full documentation
- [ ] session_memory.md updated with complete work log

---

## Next Steps (Awaiting Approval)

1. **Review this plan** - Do you approve the structure, phases, and approach?
2. **Confirm API keys are secure** - Tavily key will be in .env only, not in code
3. **Approve timeline** - Estimated 4 hours total
4. **Confirm deliverables** - Main notebook + testing notebook + LaTeX/PDF report

Once approved, I'll proceed with:
- Phase 1: Setup configuration files
- Phase 2-3: Implement the workflow
- Phase 4-5: Test and evaluate
- Phase 6-7: Generate report and commit

---

## Big Picture Vision

This HealthBot demonstrates key LangGraph concepts:
- Multi-step workflow orchestration
- Complex state management
- Tool integration (Tavily search)
- LLM chaining and evaluation
- User interaction in graphs
- Session management and reset

Upon completion, HealthBot will be a portfolio-quality project showing:
- End-to-end AI agent development
- Production-ready architecture
- Comprehensive documentation
- Testing and evaluation methodology
