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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    healthbot_dir = os.path.dirname(current_dir)  # healthbot/
    project_dir = os.path.dirname(healthbot_dir)  # project/
    
    env_path = os.path.join(project_dir, ".env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
        return True
    return False

def initialize_llm():
    """
    Initialize ChatOpenAI using Azure Foundry credentials from root .env
    
    Expected environment variables:
    - FOUNDRY_PROJECT_ENDPOINT
    - FOUNDRY_PROJECT_REGION
    - FOUNDRY_DEPLOYMENT_NAME
    - FOUNDRY_API_KEY
    """
    
    # Load credentials from root .env
    if not load_env_from_root():
        raise EnvironmentError("Could not find .env file at workspace root")
    
    # Get Azure Foundry credentials
    api_base = os.getenv("FOUNDRY_PROJECT_ENDPOINT")
    api_key = os.getenv("FOUNDRY_API_KEY")
    deployment_name = os.getenv("FOUNDRY_DEPLOYMENT_NAME")
    
    if not all([api_base, api_key, deployment_name]):
        raise EnvironmentError(
            "Missing Azure Foundry credentials. "
            "Ensure .env contains FOUNDRY_PROJECT_ENDPOINT, "
            "FOUNDRY_API_KEY, and FOUNDRY_DEPLOYMENT_NAME"
        )
    
    # Try OpenAI first (if available), fallback to Azure Foundry
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if openai_key:
        # Use OpenAI ChatGPT
        llm = ChatOpenAI(
            api_key=openai_key,
            model="gpt-3.5-turbo",
            temperature=0.7,
        )
        return llm
    
    # Fallback to Azure Foundry
    if not all([api_base, api_key, deployment_name]):
        raise EnvironmentError(
            "Missing credentials. Need either OPENAI_API_KEY or "
            "(FOUNDRY_PROJECT_ENDPOINT + FOUNDRY_API_KEY + FOUNDRY_DEPLOYMENT_NAME)"
        )
    
    # Initialize ChatOpenAI with Azure Foundry endpoint
    llm = ChatOpenAI(
        model_name=deployment_name,
        api_key=api_key,
        base_url=api_base,
        temperature=0.7,
    )
    
    return llm

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
