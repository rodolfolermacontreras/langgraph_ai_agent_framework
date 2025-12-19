"""
HealthBot Workflow
LangGraph workflow orchestrating all 8 nodes
"""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.runnables import RunnableConfig

from state import State
from nodes import (
    ask_for_topic,
    search_medical_info,
    summarize_results,
    present_summary,
    generate_quiz,
    present_quiz,
    evaluate_answer,
    ask_continue,
)


def create_healthbot_workflow():
    """
    Create and compile the HealthBot LangGraph workflow
    
    Workflow:
    START -> ask_for_topic -> search_medical_info -> summarize_results ->
    present_summary -> generate_quiz -> present_quiz -> evaluate_answer ->
    ask_continue -> [ask_for_topic (continue) OR END (exit)]
    
    Returns:
        Compiled workflow (CompiledGraph)
    """
    
    # Create workflow
    workflow = StateGraph(State)
    
    # Add all 8 nodes
    workflow.add_node("ask_for_topic", ask_for_topic)
    workflow.add_node("search_medical_info", search_medical_info)
    workflow.add_node("summarize_results", summarize_results)
    workflow.add_node("present_summary", present_summary)
    workflow.add_node("generate_quiz", generate_quiz)
    workflow.add_node("present_quiz", present_quiz)
    workflow.add_node("evaluate_answer", evaluate_answer)
    workflow.add_node("ask_continue", ask_continue)
    
    # Define edges (linear workflow with conditional at end)
    workflow.add_edge(START, "ask_for_topic")
    workflow.add_edge("ask_for_topic", "search_medical_info")
    workflow.add_edge("search_medical_info", "summarize_results")
    workflow.add_edge("summarize_results", "present_summary")
    workflow.add_edge("present_summary", "generate_quiz")
    workflow.add_edge("generate_quiz", "present_quiz")
    workflow.add_edge("present_quiz", "evaluate_answer")
    workflow.add_edge("evaluate_answer", "ask_continue")
    
    # Conditional edge: route based on patient's choice
    def route_user_choice(state):
        """
        Route based on patient's choice after seeing grade:
        - 'more_questions': Generate another quiz on same topic
        - 'new_topic': Start fresh with new health topic
        - 'exit': End the session
        """
        choice = state.get("should_continue", "exit")
        
        if choice == "more_questions":
            return "generate_quiz"  # Go back to generate another question
        elif choice == "new_topic":
            return "ask_for_topic"  # Start fresh
        else:  # exit
            return "end"
    
    workflow.add_conditional_edges(
        "ask_continue",
        route_user_choice,
        {
            "generate_quiz": "generate_quiz",
            "ask_for_topic": "ask_for_topic",
            "end": END
        }
    )
    
    # Compile with memory checkpointer
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)
    
    return app


def create_config(thread_id="healthbot_session_default", recursion_limit=2000):
    """
    Create runtime configuration for workflow execution
    
    Args:
        thread_id: Unique session identifier
        recursion_limit: Maximum recursion depth
        
    Returns:
        RunnableConfig
    """
    return RunnableConfig(
        recursion_limit=recursion_limit,
        configurable={"thread_id": thread_id}
    )


def initialize_empty_state():
    """
    Create initial empty state for workflow
    
    Returns:
        Initial State
    """
    return {
        "messages": [],
        "health_topic": None,
        "search_results": None,
        "summary": None,
        "quiz_question": None,
        "patient_answer": None,
        "grade": None,
        "feedback": None,
        "should_continue": None,
        "session_id": None,
        "quiz_count": 0,
    }
