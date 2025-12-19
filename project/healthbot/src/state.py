"""
HealthBot State Schema
Defines the structure of state throughout the workflow
"""

from typing import Optional, List
from langgraph.graph import MessagesState

class State(MessagesState):
    """
    Extended MessagesState for HealthBot workflow
    
    Inherits from MessagesState:
    - messages: List of chat messages
    
    Additional fields:
    - health_topic: Current health topic user wants to learn about
    - search_results: Raw search results from Tavily
    - summary: Patient-friendly summary of medical information
    - quiz_question: Generated comprehension check question
    - patient_answer: Patient's answer to quiz question
    - grade: Numeric grade for answer (0-100)
    - feedback: Detailed feedback with citations
    - should_continue: Whether patient wants to learn another topic
    - session_id: Unique session identifier
    """
    
    health_topic: Optional[str] = None
    search_results: Optional[str] = None
    summary: Optional[str] = None
    quiz_question: Optional[str] = None
    patient_answer: Optional[str] = None
    grade: Optional[int] = None
    feedback: Optional[str] = None
    should_continue: Optional[bool] = None
    session_id: Optional[str] = None

def reset_for_new_topic(state: State) -> State:
    """
    Reset state for a new health topic while preserving session continuity
    
    Clears topic-specific data but keeps messages and session_id
    
    Args:
        state: Current workflow state
        
    Returns:
        Reset state with cleared topic-specific fields
    """
    # Keep session_id and messages for continuity, clear topic-specific fields
    state["health_topic"] = None
    state["search_results"] = None
    state["summary"] = None
    state["quiz_question"] = None
    state["patient_answer"] = None
    state["grade"] = None
    state["feedback"] = None
    state["should_continue"] = None
    
    return state
