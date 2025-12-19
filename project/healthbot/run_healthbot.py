#!/usr/bin/env python
"""
HealthBot - Patient Education AI Agent
Main execution script - runs workflow in fresh Python process
"""

import sys
import os
from dotenv import load_dotenv

# Add src to path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

# Load environment - .env is at project root (up 2 levels from this file)
env_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(env_file)

print(f"Loading .env from: {env_file}")
print(f"File exists: {os.path.exists(env_file)}")

# Verify credentials
assert os.getenv('FOUNDRY_PROJECT_ENDPOINT'), "Missing FOUNDRY_PROJECT_ENDPOINT"
assert os.getenv('FOUNDRY_API_KEY'), "Missing FOUNDRY_API_KEY"
assert os.getenv('TAVILY_API_KEY'), "Missing TAVILY_API_KEY"

print("✓ Environment loaded")
print("✓ Credentials verified")

# Import workflow
from workflow import create_healthbot_workflow, create_config, initialize_empty_state

print("✓ Modules imported")

# Create workflow
app = create_healthbot_workflow()
print("✓ Workflow created")

# Initialize
config = create_config(thread_id="healthbot_session_cli")
initial_state = initialize_empty_state()

# Run
print("\n" + "="*80)
print("STARTING HEALTHBOT SESSION")
print("="*80)
print("\nFollow the prompts to interact with HealthBot")
print("Tips:")
print("  - Enter health topics (e.g., 'diabetes', 'hypertension', 'heart disease')")
print("  - Read the summary carefully before answering the quiz")
print("  - Answer quiz questions in your own words")
print("  - After grading, choose to: answer more questions, learn a new topic, or exit")
print("\n" + "="*80 + "\n")

try:
    final_state = app.invoke(initial_state, config)
    
    print("\n" + "="*80)
    print("SESSION COMPLETE")
    print("="*80)
    print(f"\nMessages exchanged: {len(final_state['messages'])}")
    print(f"Final topic: {final_state.get('health_topic', 'N/A')}")
    print(f"Final grade: {final_state.get('grade', 'N/A')}/100")
    print(f"Quiz count: {final_state.get('quiz_count', 0)}")
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
