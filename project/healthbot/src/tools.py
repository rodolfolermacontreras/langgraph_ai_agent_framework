"""
HealthBot Tools
Tavily search integration for medical information retrieval
"""

import os
from dotenv import load_dotenv
from tavily import TavilyClient

def load_env_from_project_root():
    """Load .env from project root"""
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    # From src/ go up 2 levels to project/
    project_root = os.path.dirname(os.path.dirname(current_file_dir))
    env_path = os.path.join(project_root, ".env")
    
    if os.path.exists(env_path):
        load_dotenv(env_path)
        return True
    return False

def search_medical_information(topic: str, max_results: int = 5) -> str:
    """
    Search for medical information using Tavily API
    
    Args:
        topic: Health topic to search for
        max_results: Number of results to return
        
    Returns:
        Formatted search results as string
    """
    # Load environment
    load_env_from_project_root()
    
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        raise EnvironmentError("TAVILY_API_KEY not found in project/.env")
    
    # Use Tavily client directly (no LangChain wrapper)
    client = TavilyClient(api_key=api_key)
    
    # Build search query
    query = f"{topic} patient education medical information"
    
    try:
        # Execute search
        results = client.search(query, max_results=max_results)
        
        # Format results
        output = ""
        if results and "results" in results:
            for i, result in enumerate(results["results"], 1):
                title = result.get("title", "Untitled")
                url = result.get("url", "")
                content = result.get("content", "")
                
                output += f"\n{i}. {title}\n"
                output += f"   Source: {url}\n"
                output += f"   {content[:300]}...\n"
        
        return output if output else "No search results found"
        
    except Exception as e:
        raise Exception(f"Tavily search failed: {str(e)}")


if __name__ == "__main__":
    # Test
    try:
        results = search_medical_information("diabetes", max_results=2)
        print("Search successful:")
        print(results)
    except Exception as e:
        print(f"Error: {e}")

