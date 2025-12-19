"""
HealthBot Workflow Nodes
8 core conversation nodes for the HealthBot workflow
"""

from langchain_core.messages import AIMessage, HumanMessage
from src.state import State, reset_for_new_topic
from src.utils import (
    display_text_to_user,
    ask_user_for_input,
    validate_non_empty_input,
    validate_topic_length,
    separator,
)
from src.tools import search_medical_information
from src.llm_config import initialize_llm


# ============================================================================
# NODE 1: Ask for Health Topic
# ============================================================================

def ask_for_topic(state: State) -> State:
    """
    NODE 1: Greet patient and ask what health topic they want to learn about
    
    Output:
    - health_topic: Set with user's topic
    - messages: Updated with greeting and patient input
    """
    
    greeting = """
    ================================================================================
    Welcome to HealthBot - Your Personal Health Education Assistant
    ================================================================================
    
    I'm here to help you learn about health topics and medical conditions in 
    simple, easy-to-understand language.
    
    """
    
    display_text_to_user(greeting)
    
    # Ask for health topic
    prompt = "What health topic or medical condition would you like to learn about? "
    
    try:
        topic = ask_user_for_input(prompt)
        validate_non_empty_input(topic, "Health topic")
        validate_topic_length(topic)
    except ValueError as e:
        display_text_to_user(f"Error: {str(e)}")
        # Retry recursively (in production, add retry limit)
        return ask_for_topic(state)
    
    # Update state
    state["health_topic"] = topic
    state["messages"].append(HumanMessage(content=f"I want to learn about: {topic}"))
    state["messages"].append(AIMessage(content=f"Great! Let me find information about {topic} for you..."))
    
    return state


# ============================================================================
# NODE 2: Search Medical Information
# ============================================================================

def search_medical_info(state: State) -> State:
    """
    NODE 2: Search Tavily for relevant medical information
    
    Input:
    - health_topic: The topic to search for
    
    Output:
    - search_results: Raw Tavily search results
    - messages: Updated with search status
    """
    
    topic = state.get("health_topic", "")
    
    if not topic:
        raise ValueError("Health topic not set before search")
    
    display_text_to_user(f"Searching for medical information about '{topic}'...")
    
    try:
        results = search_medical_information(topic)
        state["search_results"] = results
        state["messages"].append(
            AIMessage(content=f"Found information about {topic}. Now creating a summary...")
        )
    except Exception as e:
        error_msg = f"Error searching for medical information: {str(e)}"
        display_text_to_user(error_msg)
        raise
    
    return state


# ============================================================================
# NODE 3: Summarize Results
# ============================================================================

def summarize_results(state: State) -> State:
    """
    NODE 3: Summarize search results into patient-friendly language
    
    Input:
    - search_results: Raw Tavily search results
    - health_topic: The health topic
    
    Output:
    - summary: Patient-friendly summary
    - messages: Updated with summary prompt
    """
    
    search_results = state.get("search_results", "")
    topic = state.get("health_topic", "")
    
    if not search_results:
        raise ValueError("No search results to summarize")
    
    # Initialize LLM
    llm = initialize_llm()
    
    # Create summarization prompt
    summarization_prompt = f"""
You are a healthcare educator. Your task is to create a simple, patient-friendly 
explanation of medical information.

Health Topic: {topic}

Medical Information (from web search):
{search_results}

Please create a clear summary that:
1. Explains the condition in simple language (8th grade reading level)
2. Covers: what it is, symptoms, causes, and treatment options
3. Is 300-400 words maximum
4. Includes citations or references to the sources
5. Avoids medical jargon or explains it clearly

Patient-Friendly Summary:
"""
    
    try:
        response = llm.invoke(summarization_prompt)
        summary = response.content
        state["summary"] = summary
        state["messages"].append(AIMessage(content="Summary created successfully."))
    except Exception as e:
        error_msg = f"Error summarizing results: {str(e)}"
        display_text_to_user(error_msg)
        raise
    
    return state


# ============================================================================
# NODE 4: Present Summary to Patient
# ============================================================================

def present_summary(state: State) -> State:
    """
    NODE 4: Display summary and wait for patient to read it
    
    Input:
    - summary: Patient-friendly summary
    
    Output:
    - messages: Updated with patient acknowledgment
    """
    
    summary = state.get("summary", "")
    
    if not summary:
        raise ValueError("No summary to present")
    
    display = f"""
{separator('=', 80)}
HEALTH INFORMATION SUMMARY
{separator('=', 80)}

{summary}

{separator('=', 80)}
"""
    
    display_text_to_user(display)
    
    # Wait for patient to finish reading
    prompt = "Have you finished reading? Type 'ready' to proceed to the comprehension check: "
    
    response = ask_user_for_input(prompt)
    
    while response.lower() != 'ready':
        display_text_to_user("Please type 'ready' when you're finished reading.")
        response = ask_user_for_input(prompt)
    
    state["messages"].append(HumanMessage(content="I've finished reading and I'm ready for the quiz"))
    state["messages"].append(AIMessage(content="Great! Let me create a quiz question to check your understanding."))
    
    return state


# ============================================================================
# NODE 5: Generate Quiz Question
# ============================================================================

def generate_quiz(state: State) -> State:
    """
    NODE 5: Generate a comprehension check question
    
    Input:
    - summary: Patient-friendly summary to base question on
    - health_topic: The health topic
    - quiz_count: Number of quizzes already done on this topic
    
    Output:
    - quiz_question: Generated quiz question (different from previous)
    - quiz_count: Incremented by 1
    - messages: Updated with quiz intro
    
    Stand-out Feature: Generates different questions for multiple quizzes on same topic
    """
    
    summary = state.get("summary", "")
    topic = state.get("health_topic", "")
    quiz_count = state.get("quiz_count", 0)
    quiz_count += 1
    
    if not summary:
        raise ValueError("No summary available for quiz generation")
    
    # Initialize LLM
    llm = initialize_llm()
    
    # Create quiz prompt (request different question if this is a repeat quiz)
    additional_instruction = ""
    if quiz_count > 1:
        additional_instruction = f"\n\nNote: This is quiz question #{quiz_count} on this topic. Please generate a DIFFERENT question that tests a different aspect or concept from the summary than previous questions."
    
    # Create quiz prompt
    quiz_prompt = f"""
You are a healthcare educator creating a simple quiz to test patient understanding.

Health Topic: {topic}

Patient-Friendly Summary:
{summary}

Create ONE quiz question that tests understanding of key points from the summary. 

The question should:
1. Be clear and simple (8th grade reading level)
2. Test understanding, not memorization
3. Be answerable based on the summary
4. Be relevant to patient education{additional_instruction}

Format your response as ONLY the question (no numbering, no answer choices unless 
you're doing multiple choice). If you create multiple choice, include options A, B, C, D.

Quiz Question:
"""
    
    try:
        response = llm.invoke(quiz_prompt)
        quiz_question = response.content.strip()
        state["quiz_question"] = quiz_question
        state["quiz_count"] = quiz_count
        
        question_label = f"(Question {quiz_count})" if quiz_count > 1 else ""
        state["messages"].append(AIMessage(content=f"Quiz {question_label}: {quiz_question}"))
    except Exception as e:
        error_msg = f"Error generating quiz question: {str(e)}"
        display_text_to_user(error_msg)
        raise
    
    return state


# ============================================================================
# NODE 6: Present Quiz and Get Answer
# ============================================================================

def present_quiz(state: State) -> State:
    """
    NODE 6: Display quiz question and get patient's answer
    
    Input:
    - quiz_question: The quiz question to ask
    - quiz_count: Which question number this is
    
    Output:
    - patient_answer: Patient's response
    - messages: Updated with question and answer
    """
    
    quiz_question = state.get("quiz_question", "")
    quiz_count = state.get("quiz_count", 1)
    
    if not quiz_question:
        raise ValueError("No quiz question available")
    
    display = f"""
{separator('=', 80)}
COMPREHENSION CHECK QUIZ - Question {quiz_count}
{separator('=', 80)}

{quiz_question}

{separator('=', 80)}
"""
    
    display_text_to_user(display)
    
    # Get patient's answer
    prompt = "Please enter your answer: "
    answer = ask_user_for_input(prompt)
    
    validate_non_empty_input(answer, "Quiz answer")
    
    state["patient_answer"] = answer
    state["messages"].append(HumanMessage(content=f"My answer: {answer}"))
    
    return state


# ============================================================================
# NODE 7: Evaluate Answer and Grade
# ============================================================================

def evaluate_answer(state: State) -> State:
    """
    NODE 7: Grade the patient's answer with explanation and citations
    
    Input:
    - patient_answer: Patient's quiz answer
    - quiz_question: The quiz question
    - summary: The health information summary (for citations)
    
    Output:
    - grade: Numeric grade 0-100
    - feedback: Explanation with citations
    - messages: Updated with grade and feedback
    """
    
    answer = state.get("patient_answer", "")
    question = state.get("quiz_question", "")
    summary = state.get("summary", "")
    topic = state.get("health_topic", "")
    
    if not all([answer, question, summary]):
        raise ValueError("Missing required fields for evaluation")
    
    # Initialize LLM
    llm = initialize_llm()
    
    # Create grading prompt
    grading_prompt = f"""
You are a healthcare educator grading a patient's quiz answer.

Health Topic: {topic}

Medical Summary:
{summary}

Quiz Question:
{question}

Patient's Answer:
{answer}

Please grade this answer on a scale of 0-100 points. Consider:
- Is the answer correct/accurate?
- Does it show understanding of key concepts?
- Is it partially correct?

Provide:
1. A numeric grade (0-100)
2. An explanation of the grade (2-3 sentences)
3. One or two citations/references from the summary that support the correct answer

Format your response exactly as:
GRADE: [number]
EXPLANATION: [your explanation with citations from the summary]

Example format:
GRADE: 85
EXPLANATION: Good understanding! You correctly identified [concept]. The summary notes that [citation from summary]. Consider also that [another point].
"""
    
    try:
        response = llm.invoke(grading_prompt)
        grading_result = response.content.strip()
        
        # Parse grade and feedback
        lines = grading_result.split('\n')
        grade = 0
        feedback = ""
        
        for i, line in enumerate(lines):
            if line.startswith("GRADE:"):
                try:
                    grade_str = line.replace("GRADE:", "").strip()
                    grade = int(''.join(filter(str.isdigit, grade_str)))
                    grade = min(100, max(0, grade))  # Clamp 0-100
                except ValueError:
                    grade = 70  # Default if parsing fails
            elif line.startswith("EXPLANATION:"):
                feedback = line.replace("EXPLANATION:", "").strip()
                # Append any remaining lines
                if i + 1 < len(lines):
                    feedback += "\n" + "\n".join(lines[i+1:])
                break
        
        state["grade"] = grade
        state["feedback"] = feedback
        state["messages"].append(
            AIMessage(content=f"Grade: {grade}/100\n\n{feedback}")
        )
        
    except Exception as e:
        error_msg = f"Error evaluating answer: {str(e)}"
        display_text_to_user(error_msg)
        raise
    
    return state


# ============================================================================
# NODE 8: Ask to Continue
# ============================================================================

def ask_continue(state: State) -> State:
    """
    NODE 8: Present grade/feedback and ask what patient wants to do next
    
    Input:
    - grade: Patient's grade
    - feedback: Explanation of grade
    
    Output:
    - should_continue: 'new_topic' (new health topic), 'more_questions' (more quiz on same topic), or 'exit'
    - messages: Updated with continuation prompt
    
    Supports stand-out feature: Allow multiple quiz questions per topic
    """
    
    grade = state.get("grade", 0)
    feedback = state.get("feedback", "")
    
    display = f"""
{separator('=', 80)}
YOUR QUIZ RESULTS
{separator('=', 80)}

Grade: {grade}/100

{feedback}

{separator('=', 80)}
"""
    
    display_text_to_user(display)
    
    # Ask what patient wants to do next
    prompt = """
What would you like to do next?
  (1) Another quiz question on this topic
  (2) Learn about a new health topic
  (3) Exit the session
  
Enter your choice (1, 2, or 3): """
    
    response = ask_user_for_input(prompt).lower().strip()
    
    valid_responses = {
        '1': 'more_questions',
        '2': 'new_topic',
        '3': 'exit',
        'more_questions': 'more_questions',
        'new_topic': 'new_topic',
        'exit': 'exit',
    }
    
    while response not in valid_responses:
        display_text_to_user("Please enter '1', '2', or '3'")
        response = ask_user_for_input(prompt).lower().strip()
    
    choice = valid_responses[response]
    state["should_continue"] = choice
    
    if choice == 'more_questions':
        state["messages"].append(
            HumanMessage(content="I'd like another quiz question on this topic")
        )
        state["messages"].append(
            AIMessage(content="Great! Let me create another quiz question about this topic...")
        )
    elif choice == 'new_topic':
        state["messages"].append(
            HumanMessage(content="I'd like to learn about another topic")
        )
        # Reset state for new topic but keep session continuity
        state = reset_for_new_topic(state)
    else:  # exit
        state["messages"].append(
            HumanMessage(content="I'm done learning. Thank you!")
        )
        display_text_to_user(
            "\nThank you for using HealthBot! Stay informed, stay healthy.\n"
        )
    
    return state
