# HealthBot: AI-Powered Patient Education System

**Course**: AI Agents with LangChain and LangGraph (Udacity)  
**Student**: Rodolfo Lerma  
**Date**: December 19, 2025

---

## Project Overview

HealthBot is an intelligent patient education chatbot built with LangGraph that guides patients through learning about health topics and medical conditions. The system uses web search (Tavily), LLM-powered summarization, and comprehension quizzes to create an engaging, educational experience.

**Key Features**:
- Natural conversation flow with 8 workflow nodes
- Real-time medical information retrieval via Tavily
- Patient-friendly summaries (8th grade reading level)
- Automated quiz generation and grading
- Session management with state reset for privacy
- Azure Foundry LLM integration
- **Stand-Out Feature**: Multiple quiz questions per topic without restarting the conversation

---

## Workflow Architecture

The HealthBot follows a structured 8-node LangGraph workflow with conditional routing to support multiple quiz questions per topic (stand-out feature):

```
START
  |
  v
[1] Ask for Topic (patient input)
  |
  v
[2] Search Medical Info (Tavily)
  |
  v
[3] Summarize Results (LLM)
  |
  v
[4] Present Summary (patient review)
  |
  v
[5] Generate Quiz (LLM)
  |
  v
[6] Present Quiz (patient answer)
  |
  v
[7] Evaluate Answer (grade + feedback)
  |
  v
[8] Ask Continue
  |
  +---> "more_questions" --> back to [5] (different question, same topic)
  |---> "new_topic" --> back to [1] (reset state, new topic)
  +---> "exit" --> END
```

**Stand-Out Feature**: The "more_questions" path generates fresh quiz questions on the same topic, maintaining the summary context while testing deeper understanding.

### Node Descriptions

| Node | Input | Output | Purpose |
|------|-------|--------|---------|
| Ask for Topic | greeting | health_topic | Greet patient, get learning topic |
| Search Medical Info | health_topic | search_results | Query Tavily for medical info |
| Summarize Results | search_results | summary | Create patient-friendly summary |
| Present Summary | summary | ready_signal | Display summary, wait for readiness |
| Generate Quiz | summary | quiz_question | LLM creates comprehension question |
| Present Quiz | quiz_question | patient_answer | Display question, get answer |
| Evaluate Answer | patient_answer, summary | grade, feedback | Grade with citations |
| Ask Continue | grade | should_continue | Ask for new topic or exit |

---

## Project Structure

```
project/healthbot/
|-- src/                              # Core Python modules
|   |-- llm_config.py                 # Azure Foundry LLM initialization
|   |-- tools.py                      # Tavily search integration
|   |-- state.py                      # State schema definition
|   |-- nodes.py                      # 8 workflow node implementations
|   |-- workflow.py                   # LangGraph workflow orchestration
|   |-- utils.py                      # Helper functions (display, input, validation)
|
|-- notebooks/
|   |-- 01_healthbot_main.ipynb       # Main execution notebook
|   |-- 02_testing.ipynb              # Testing and validation
|
|-- config/
|   |-- env.example                   # Environment variable template
|   |-- settings.yaml                 # Project settings and constants
|
|-- README.md                         # This file
```

---

## Setup Instructions

### 1. Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Virtual environment (`.venv`)

### 2. Dependencies

All required packages are listed at the top of `01_healthbot_main.ipynb`:
- langchain==0.2.16
- langchain_openai==0.1.23
- langgraph==0.2.19
- langchainhub==0.1.21
- tavily-python==0.4.0
- langchain-community==0.2.16
- python-dotenv==1.0.1

### 3. Environment Configuration

**Using the workspace .env** (root level):

The HealthBot uses the existing `.env` file at the workspace root with these variables:
```
FOUNDRY_PROJECT_ENDPOINT=https://langgraph-exploration-resource.services.ai.azure.com/api/projects/langgraph-exploration
FOUNDRY_PROJECT_REGION=westus
FOUNDRY_DEPLOYMENT_NAME=gpt-4.1
FOUNDRY_API_KEY=your-api-key
TAVILY_API_KEY=tvly-xxxxxxxxxxxx
```

**To set up Tavily API key**:
1. Sign up free at https://app.tavily.com/home
2. Get your API key from https://app.tavily.com/home
3. Add `TAVILY_API_KEY=tvly-xxxxx` to the root `.env` file (first 1000 requests free)

**Do NOT commit the .env file** - API keys must remain private.

### 4. Running HealthBot

Navigate to the project folder and run:

```bash
cd project/healthbot
jupyter notebook notebooks/01_healthbot_main.ipynb
```

Then execute all cells in order. The notebook will:
1. Verify all environment variables
2. Initialize the LLM and search tools
3. Create the LangGraph workflow
4. Display the workflow diagram
5. Start an interactive HealthBot session

---

## Key Design Decisions

### 1. Azure Foundry instead of OpenAI
- Already configured in workspace
- Cost-effective for learning
- Same LangChain interface

### 2. Modular Node Architecture
- Each node is independently testable
- Clear separation of concerns
- Easy to debug and modify

### 3. State-Based Workflow (vs. Message Chain)
- Better tracking of workflow state
- Supports complex branching
- Enables proper session reset
- Maintains privacy between topics

### 4. Patient-Friendly Language
- LLM-driven summarization
- 8th grade reading level
- Medical accuracy preserved
- Accessible to all education levels

### 5. Citation-Based Grading
- References support correct answers
- Enhances learning value
- Builds trust in AI responses
- Helps patients verify information

### 6. Security-First Configuration
- All secrets in `.env` (never in code)
- Template provided for others
- Easy migration to production

---

## Usage Example

**Typical HealthBot Conversation with Stand-Out Feature** (Multiple Questions):

```
HealthBot: "Welcome to HealthBot! What health topic would you like to learn about?"
Patient:  "I want to learn about diabetes"

[HealthBot searches Tavily for diabetes information]

HealthBot: [Displays patient-friendly summary about diabetes, symptoms, treatment]

HealthBot: "Have you finished reading? Type 'ready' to proceed to comprehension check"
Patient:  "ready"

HealthBot: "COMPREHENSION CHECK QUIZ - Question 1
           Which of the following is a symptom of type 2 diabetes?
           A) Increased thirst
           B) Weight gain
           C) Frequent urination
           D) All of the above"
Patient:  "D"

HealthBot: "Grade: 95/100
           Excellent! You correctly identified multiple symptoms. The summary notes that 
           'increased thirst, weight gain, and frequent urination' are common symptoms..."

HealthBot: "What would you like to do next?
           (1) Another quiz question on this topic
           (2) Learn about a new health topic
           (3) Exit the session
           
           Enter your choice (1, 2, or 3):"
Patient:  "1"

HealthBot: "Great! Let me create another quiz question about this topic..."

HealthBot: "COMPREHENSION CHECK QUIZ - Question 2
           What is the primary cause of type 2 diabetes?
           A) Pancreas produces no insulin
           B) Body cannot use insulin effectively
           C) Viral infection
           D) Lack of exercise alone"
Patient:  "B"

HealthBot: "Grade: 100/100
           Perfect! Type 2 diabetes is characterized by insulin resistance, where the body 
           produces insulin but cannot use it effectively. This is different from type 1, 
           where the pancreas doesn't produce insulin..."

HealthBot: "What would you like to do next?
           (1) Another quiz question on this topic
           (2) Learn about a new health topic
           (3) Exit the session"
Patient:  "2"

HealthBot: [State resets, returns to topic selection]
HealthBot: "What health topic would you like to learn about?"
Patient:  "hypertension"

[Workflow continues with new topic...]
```

**Key Feature Highlights**:
- Question 1 vs Question 2 are different but both from same summary
- Same topic context maintained across multiple questions
- Patient can switch topics anytime or exit
- State resets cleanly when starting new topic

---

## Testing

See `02_testing.ipynb` for:
- Individual node testing
- Error handling validation
- LLM output quality checks
- Tavily search verification
- State reset verification
- End-to-end workflow tests

---

## Development Notes

### Code Structure
- **Separation of Concerns**: Each module has a single responsibility
- **Error Handling**: Graceful failures with clear error messages
- **Validation**: Input validation at each node
- **Logging**: Key decision points logged to state

### Workflow Control Flow
- Linear progression through 8 nodes
- Conditional branching at end (continue or exit)
- State reset when starting new topic
- Session continuity maintained via messages

### LLM Prompting Strategy
- Specific, role-based prompts (healthcare educator)
- Output format specification
- Examples provided where helpful
- Temperature tuned for balance (0.7 - not too rigid, not too creative)

---

## Performance Considerations

- **Tavily Quota**: 1000 free requests/month for development
- **LLM Latency**: Expect 2-5 seconds per LLM call
- **Memory Usage**: State stored in-memory via MemorySaver
- **Scalability**: For production, use persistent storage instead of memory

---

## Stand-Out Features Implemented

**Multiple Quiz Questions Per Topic** (IMPLEMENTED):
- Patients can request additional quiz questions on the same topic without restarting
- Each question is generated fresh and tests different aspects of the summary
- Maintains conversation continuity and topic context
- Increases educational value by allowing deeper knowledge verification

---

## Future Enhancements

1. **Difficulty Settings**: Adapt summary length and question complexity based on user preference
2. **Related Subjects**: Suggest related topics at end of session (e.g., "Learn about complications of diabetes next?")
3. **Progress Tracking**: Store learning history across sessions
4. **Personalization**: Adjust pacing and difficulty based on user performance
5. **Knowledge Base**: Integrate curated medical knowledge base for consistency
6. **Accessibility**: Text-to-speech and speech-to-text support
7. **Analytics**: Track common questions and knowledge gaps
8. **Multi-language**: Support for non-English languages

---

## Troubleshooting

### "Missing FOUNDRY_API_KEY"
- Verify `.env` file exists at workspace root
- Check Azure credentials are correct
- Ensure API key has not expired

### "Missing TAVILY_API_KEY"
- Sign up at https://app.tavily.com/home
- Add API key to root `.env` file
- Restart notebook kernel after updating `.env`

### "LLM response is too long/short"
- Adjust `LLM_MAX_TOKENS` in `config/settings.yaml`
- Modify prompt templates in `nodes.py`
- Test with different temperature values

### "Tavily search returns poor results"
- Verify Tavily account is active
- Check search query is specific enough
- Try different health topic wording

---

## References

- **LangGraph Documentation**: https://langchain-ai.github.io/langgraph/
- **LangChain Documentation**: https://python.langchain.com/
- **Tavily API**: https://tavily.com/
- **Azure Foundry**: https://learn.microsoft.com/en-us/azure/ai-services/

---

## License

This project is created as part of the Udacity AI Agents course and is for educational purposes.

---

## Contact & Support

For issues or questions about this project, refer to the Udacity course materials or contact the course instructor.

---

**Last Updated**: December 19, 2025  
**Status**: Complete - Ready for Testing and Evaluation
