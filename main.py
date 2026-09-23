import os
from dotenv import load_dotenv

# 1. Load the variables from the .env file into the system memory
load_dotenv()

# 2. Retrieve the variables using the standard os module
app_name = os.getenv("APP_NAME")
api_key = os.getenv("AI_API_KEY")
missing_val = os.getenv("DATABASE_URL")

if not api_key:
    raise ValueError("AI_API_KEY is missing! Please set it in your .env file.")
    
print(f"Missing variable is: {missing_val}")

print(f"Starting application: {app_name}")
print(f"Retrieved API Key: {api_key}")