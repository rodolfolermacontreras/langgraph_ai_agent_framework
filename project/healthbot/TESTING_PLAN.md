# HealthBot Testing & Validation Plan

**Date**: December 19, 2025  
**Status**: Ready for Phase 4 Testing

---

## Testing Objectives

Validate HealthBot against the official Udacity rubric and verify all features work correctly:

1. **Rubric Compliance**: All required features implemented and working
2. **Functionality**: End-to-end workflow execution
3. **Quality**: Information accuracy, user experience, error handling
4. **Stand-Out Features**: Multiple quiz questions per topic

---

## Rubric Validation Checklist

### Criteria 1: Model and Tools LangGraph Configuration

**Requirement**: API keys loaded correctly, successful API calls to Tavily and Azure Foundry, OpenAI/Azure calls Tavily for search

**Test Plan**:
- [ ] Run notebook - should load environment variables without errors
- [ ] Verify console output shows "All environment variables loaded successfully!"
- [ ] First workflow node executes (ask_for_topic)
- [ ] Second workflow node executes (search_medical_info) - makes Tavily API call
- [ ] Tavily returns results (non-empty)

**Test Topics**:
- "diabetes"
- "hypertension"
- "heart disease"

**Success Criteria**: Tavily search returns results for all topics

**Documentation**: Screenshot showing Tavily results in console

---

### Criteria 2: Model Summarization of Search Results

**Requirement**: Model calls Tavily, receives results, uses well-written prompt to summarize, creates 3-4 paragraph summary using only those results

**Test Plan**:
- [ ] Node 3 (summarize_results) executes
- [ ] Displays 3-4 paragraph summary
- [ ] Summary uses simple language (8th grade level)
- [ ] Summary includes key concepts from the search results
- [ ] No hallucinated information (only from Tavily results)

**Validation Method**:
1. Note Tavily results content
2. Read displayed summary
3. Verify summary references match Tavily content
4. Check sentence complexity is appropriate

**Success Criteria**: Summary is 300-400 words, clear, medically accurate, derived from Tavily results

**Documentation**: Screenshot of Tavily results + displayed summary

---

### Criteria 3: Quiz Question Creation & Grading

**Requirement A - Quiz Creation**:
- Well-written prompt to create quiz using only summary data
- Question is answerable from summary alone

**Requirement B - Grading**:
- Grade answer using only summary as data source
- Provide grade (A, B, C, etc) or numeric score
- Provide justification with reasoning

**Test Plan**:
- [ ] Node 5 (generate_quiz) executes
- [ ] Displays clear quiz question
- [ ] Question is understandable and answerable from summary
- [ ] Node 7 (evaluate_answer) executes
- [ ] Provides numeric grade (0-100)
- [ ] Provides detailed explanation
- [ ] Explanation includes citations from summary

**Test Answers**:
For each topic, test with:
- Correct answer (expect high grade 80+)
- Partially correct answer (expect medium grade 50-75)
- Incorrect answer (expect low grade 0-50)

**Success Criteria**: 
- Questions are specific and answerable
- Grades are appropriate to answer quality
- Feedback includes summary citations

**Documentation**: Screenshots of questions and grades

---

### Criteria 4: LangGraph State

**Requirement**: State class created, properties for workflow data, state updated appropriately, subsequent nodes access previous data, model has access to previous messages

**Test Plan**:
- [ ] State class imported successfully (state.py)
- [ ] State has these fields:
  - messages
  - health_topic
  - search_results
  - summary
  - quiz_question
  - patient_answer
  - grade
  - feedback
  - should_continue
  - quiz_count
- [ ] Node 2 has access to health_topic (set by Node 1)
- [ ] Node 3 has access to search_results (set by Node 2)
- [ ] Node 7 has access to patient_answer, quiz_question, summary (set by previous nodes)

**Test Method**:
- Read src/state.py - verify all fields present
- Read src/nodes.py - verify nodes read from state
- Run workflow - verify no "undefined state field" errors

**Success Criteria**: All state fields properly initialized and accessible

**Documentation**: State schema diagram

---

### Criteria 5: Nodes, Edges, and Modifications

**Requirement**:
- Multiple nodes for workflow steps
- Nodes with single responsibility
- Edges configured for sequential workflow
- User can restart workflow or exit after grade
- Full workflow executes: subject → summary → quiz → grade → continue/exit

**Test Plan**:
- [ ] Verify 8 nodes exist (nodes.py)
- [ ] Each node has single clear purpose
- [ ] Workflow compiles without errors (workflow.py)
- [ ] START -> ask_for_topic edge works
- [ ] Linear progression through nodes 1-7 works
- [ ] ask_continue conditional routing works:
  - [ ] "more_questions" routes back to generate_quiz
  - [ ] "new_topic" routes back to ask_for_topic with state reset
  - [ ] "exit" routes to END
- [ ] Run full workflow start to finish
- [ ] Complete at least 1 full topic cycle
- [ ] Test "more_questions" path (answer another question)
- [ ] Test "new_topic" path (start fresh with different topic)
- [ ] Test "exit" path (end session)

**Success Criteria**: All paths work, no errors, proper routing

**Documentation**: 
- Screenshot of workflow graph (from notebook visualization)
- Console logs showing workflow progression
- Examples of each routing path

---

## Feature Testing

### Core Workflow Test

**Test Flow 1: Single Topic, Single Question, Exit**
1. Enter topic: "asthma"
2. Read summary
3. Answer quiz question
4. See grade
5. Choose "exit"

**Expected Outcomes**:
- [ ] Summary is 300-400 words, clear, medically accurate
- [ ] Quiz question is answerable from summary
- [ ] Grade is provided (0-100)
- [ ] Feedback includes citations
- [ ] Session ends cleanly

---

### Stand-Out Feature Test: Multiple Questions

**Test Flow 2: Multiple Questions on Same Topic**
1. Enter topic: "high blood pressure"
2. Read summary
3. Answer Question 1 - get grade
4. Choose "more_questions" (path 1)
5. Answer Question 2 (different question) - get grade
6. Choose "more_questions" again
7. Answer Question 3 - get grade
8. Choose "new_topic"
9. Enter new topic: "cholesterol"
10. Verify state reset (clean summary, new search, etc.)
11. Complete workflow and "exit"

**Expected Outcomes**:
- [ ] Questions 1, 2, 3 are all different
- [ ] Questions test different concepts
- [ ] Same summary used for all questions
- [ ] Each has appropriate grading
- [ ] State resets on new_topic (no carryover)
- [ ] New topic has independent summary
- [ ] No API key leakage in output

---

### Error Handling Tests

**Test empty inputs**:
- [ ] Topic input: Enter empty string -> prompt to retry
- [ ] Quiz answer: Enter empty string -> prompt to retry
- [ ] Continue choice: Enter invalid choice -> prompt to retry

**Test boundary cases**:
- [ ] Very long topic name (1000 characters)
- [ ] Special characters in topic
- [ ] Numbers in topic

---

## Quality Checks

### Information Accuracy

**Test**: Compare HealthBot's summary against authoritative sources

For each topic:
- [ ] Key facts are accurate
- [ ] No medical misinformation
- [ ] Appropriately caveated (when necessary)
- [ ] Sources are credible

**Documentation**: Side-by-side comparison of summary vs. authoritative source

---

### User Experience

**Assess**:
- [ ] Prompts are clear and understandable
- [ ] Summary is readable (8th grade level)
- [ ] Quiz questions are fair and clear
- [ ] Feedback is constructive
- [ ] Flow feels natural and conversational

---

### Code Quality

**Check**:
- [ ] No API keys visible in console output
- [ ] No API keys in any .py files
- [ ] No API keys in environment examples
- [ ] Error messages are helpful
- [ ] Code is properly documented (docstrings present)

---

## Test Execution Record

### Session 1: Core Workflow

**Topic 1: Diabetes**
- Summary length: ___ words
- Q1 Answer: ___
- Q1 Grade: ___ /100
- Test result: [PASS/FAIL]

**Topic 2: Heart Disease**
- Summary length: ___ words
- Q1 Answer: ___
- Q1 Grade: ___ /100
- Test result: [PASS/FAIL]

### Session 2: Stand-Out Feature

**Topic: Hypertension**
- Summary length: ___ words
- Q1 Answer: ___ Grade: ___ /100
- Q2 (different from Q1): Answer: ___ Grade: ___ /100
- Q3 (different from Q1 & Q2): Answer: ___ Grade: ___ /100
- New Topic: Cholesterol
- Summary is fresh (different from hypertension): [YES/NO]
- Test result: [PASS/FAIL]

---

## Required Deliverables

After testing, provide:

1. **Test Results Summary**: What passed, what failed
2. **Screenshots**: Key moments (summary display, grades, routing)
3. **Console Logs**: Full workflow execution showing node progression
4. **Issue Report**: Any bugs or unexpected behavior
5. **Rubric Compliance Report**: Checkmark each requirement

---

## Success Criteria

**All tests PASS if**:
- [x] All 8 nodes execute without errors
- [x] Tavily search returns valid results
- [x] Summaries are 3-4 paragraphs, clear, medical accurate
- [x] Quiz questions are answerable from summary
- [x] Grades are numeric and justified with citations
- [x] All state fields properly tracked
- [x] Workflow completes start to finish
- [x] Routing (continue/exit) works
- [x] Multiple questions feature works
- [x] State reset works for new topics
- [x] No API keys leaked
- [x] User experience is clear and smooth

**Project is READY FOR EVALUATION if**:
- All tests PASS
- All rubric requirements met
- Stand-out feature implemented and working
- Documentation complete

---

## Next Steps

1. Run notebook: `notebooks/01_healthbot_main.ipynb`
2. Follow test plan above
3. Document results
4. Collect evidence (screenshots, logs)
5. Update this file with test results
6. Create evaluation report
