"""
HealthBot LLM Configuration
Uses Azure Foundry endpoint from root .env file
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from root .env
# (The notebook will be in project/healthbot/notebooks/, so we go up 3 levels)
def load_env_from_root():
    """Load .env from project root (2 levels up from this file)"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        healthbot_dir = os.path.dirname(current_dir)  # healthbot/
        project_dir = os.path.dirname(healthbot_dir)  # project/
        
        env_path = os.path.join(project_dir, ".env")
        if os.path.exists(env_path):
            load_dotenv(env_path)
            return True
    except:
        # If file resolution fails (e.g., in Jupyter), try absolute path
        try:
            env_path = r"c:\Training\Udacity\AI_Agents_LangGraph\project\.env"
            if os.path.exists(env_path):
                load_dotenv(env_path)
                return True
        except:
            pass
    return False

def initialize_llm():
    """
    Initialize ChatOpenAI using credentials from environment
    Handles both CLI and notebook execution contexts
    """
    
    # Try to load .env if not already loaded
    if not os.getenv('ENV_ALREADY_LOADED'):
        # Try relative path first
        if not load_env_from_root():
            # If that fails, assume we're in a notebook with pre-loaded env
            pass
    
    # Check if we have OpenAI credentials (notebook default)
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        # Use OpenAI (notebook or CLI with OpenAI fallback)
        return ChatOpenAI(model="gpt-3.5-turbo")
    
    # Fall back to Azure Foundry
    api_base = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
    api_key = os.getenv("FOUNDRY_API_KEY")
    deployment_name = os.getenv("FOUNDRY_DEPLOYMENT_NAME")
    
    if all([api_base, api_key, deployment_name]):
        return ChatOpenAI(
            api_key=api_key,
            api_version="2024-08-01-preview",
            base_url=api_base,
            model=deployment_name
        )
    
    # If we got here, we're missing credentials
    raise EnvironmentError(
        "No valid LLM credentials found. "
        "Please ensure either OPENAI_API_KEY or FOUNDRY credentials are set in .env"
    )




def verify_tavily_api_key():
    """
    Verify Tavily API key is available
    
    Can be set in:
    1. Root .env file (TAVILY_API_KEY)
    2. config/.env file in healthbot project
    """
    
    # Try loading from root .env first
    load_env_from_root()
    
    tavily_key = os.getenv("TAVILY_API_KEY")
    
    if not tavily_key:
        raise EnvironmentError(
            "Missing TAVILY_API_KEY. "
            "Set it in root .env file or project config/.env"
        )
    
    return tavily_key

if __name__ == "__main__":
    # Test LLM initialization
    try:
        llm = initialize_llm()
        print("Successfully initialized LLM with Azure Foundry")
        print(f"Model: {llm.model_name}")
    except Exception as e:
        print(f"Error initializing LLM: {e}")
    
    # Test Tavily API key
    try:
        tavily_key = verify_tavily_api_key()
        print("Tavily API key is configured")
    except Exception as e:
        print(f"Error: {e}")
