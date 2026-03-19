import openai
import os
from dotenv import load_dotenv
import datetime

# Load your new API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # This specifically checks the usage/billing endpoint
    # Note: Modern OpenAI accounts use the 'Dashboard' for detailed billing,
    # but we can test a small call to see if the quota error persists.
    print("Checking API Key status...")
    models = openai.Model.list()
    print("✅ Connection Successful! Your key is active.")
    
    # To check actual money spent vs limit, it's best to visit:
    # https://platform.openai.com/usage
    print("\nNext Step: Visit https://platform.openai.com/usage")
    print("Look for 'Credit balance' or 'Expired' notifications.")

except openai.error.RateLimitError:
    print("❌ ERROR: Quota Exceeded.")
    print("This means your account has $0.00 balance or your free credits expired.")
except Exception as e:
    print(f"❌ An error occurred: {e}")