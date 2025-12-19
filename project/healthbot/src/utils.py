"""
HealthBot Utility Functions
Display text, get user input, and validate responses
"""

import time
import os

def display_text_to_user(text):
    """
    Display text to patient in notebook
    Includes delay to ensure text renders before asking for input
    """
    print(text)
    time.sleep(1)  # Wait for render to complete

def ask_user_for_input(prompt):
    """
    Get input from patient with validation
    
    Args:
        prompt: Input description/question
        
    Returns:
        User's response (stripped of whitespace)
    """
    response = input(prompt).strip()
    return response

def validate_non_empty_input(user_input, field_name="Input"):
    """
    Validate that input is not empty
    
    Args:
        user_input: The input to validate
        field_name: Name of field for error message
        
    Returns:
        True if valid, raises ValueError otherwise
    """
    if not user_input or len(user_input.strip()) == 0:
        raise ValueError(f"{field_name} cannot be empty")
    return True

def validate_topic_length(topic, min_length=3, max_length=500):
    """
    Validate health topic input
    
    Args:
        topic: The health topic
        min_length: Minimum length
        max_length: Maximum length
        
    Returns:
        True if valid, raises ValueError otherwise
    """
    if len(topic) < min_length:
        raise ValueError(f"Topic must be at least {min_length} characters")
    if len(topic) > max_length:
        raise ValueError(f"Topic must be no more than {max_length} characters")
    return True

def format_summary_for_display(summary, width=80):
    """
    Format summary text for readable display
    
    Args:
        summary: The summary text
        width: Line width for wrapping
        
    Returns:
        Formatted summary string
    """
    return summary  # Simple version - could add text wrapping if needed

def format_quiz_for_display(question):
    """
    Format quiz question for display
    
    Args:
        question: The quiz question
        
    Returns:
        Formatted question string
    """
    return question

def format_grade_report(grade, feedback):
    """
    Format grade and feedback for display
    
    Args:
        grade: Numeric grade (0-100)
        feedback: Feedback/explanation text
        
    Returns:
        Formatted grade report
    """
    report = f"\n{'='*50}\n"
    report += f"QUIZ RESULT\n"
    report += f"{'='*50}\n"
    report += f"Grade: {grade}/100\n\n"
    report += f"Explanation:\n{feedback}\n"
    report += f"{'='*50}\n"
    return report

def separator(char="-", length=50):
    """Create a text separator for readability"""
    return char * length
