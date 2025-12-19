"""
HealthBot Tools
Tavily search integration for medical information retrieval
"""

import os
from dotenv import load_dotenv
from langchain.agents import Tool
from tavily import TavilyClient

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
        Tavily search tool
        
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
    
    # Initialize Tavily client directly
    client = TavilyClient(api_key=tavily_api_key)
    
    return client

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
        client = initialize_tavily_search()
    except EnvironmentError as e:
        raise e
    
    # Construct search query focused on patient education
    search_query = f"{topic} patient education medical information"
    
    try:
        # Execute search using Tavily client
        results = client.search(search_query, max_results=max_results)
        
        # Format results
        formatted_results = ""
        if results and "results" in results:
            for i, result in enumerate(results["results"], 1):
                formatted_results += f"\n{i}. {result.get('title', 'No title')}\n"
                formatted_results += f"   Source: {result.get('url', 'No URL')}\n"
                formatted_results += f"   {result.get('content', 'No content')[:300]}...\n"
        
        return formatted_results if formatted_results else "No results found"
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
