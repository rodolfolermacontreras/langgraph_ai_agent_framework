"""
HealthBot Tools
Tavily search integration for medical information retrieval
"""

import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

def load_env_from_root():
    """Load .env from workspace root"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up: healthbot/src -> healthbot -> project -> root
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    env_path = os.path.join(root_dir, ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
        return True
    return False

def initialize_tavily_search():
    """
    Initialize Tavily search tool with API key from .env
    
    Returns:
        TavilySearchResults tool
        
    Raises:
        EnvironmentError if TAVILY_API_KEY not found
    """
    
    # Load from root .env
    load_env_from_root()
    
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    
    if not tavily_api_key:
        raise EnvironmentError(
            "TAVILY_API_KEY not found. "
            "Add it to root .env file (first 1000 requests free at https://app.tavily.com)"
        )
    
    # Initialize Tavily search with API key
    search = TavilySearchResults(
        api_wrapper=None,  # Let it use env variable
        max_results=5,
    )
    
    return search

def search_medical_information(topic: str, max_results: int = 5) -> str:
    """
    Search for medical information on a health topic
    
    Args:
        topic: Health topic or medical condition to search for
        max_results: Maximum number of results to return
        
    Returns:
        Formatted search results as string
        
    Raises:
        EnvironmentError if Tavily API key not configured
    """
    
    try:
        search_tool = initialize_tavily_search()
    except EnvironmentError as e:
        raise e
    
    # Construct search query focused on patient education
    search_query = f"{topic} patient education medical information"
    
    try:
        # Execute search
        results = search_tool.invoke(search_query)
        return results
    except Exception as e:
        raise Exception(f"Error searching for medical information: {str(e)}")

if __name__ == "__main__":
    # Test Tavily integration
    try:
        test_results = search_medical_information("diabetes")
        print("Tavily search successful:")
        print(test_results)
    except Exception as e:
        print(f"Error: {e}")
