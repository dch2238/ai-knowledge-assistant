# 1. Simulating an AI API call with two failure modes
def call_ai_model(prompt: str, simulate_error: bool = False) -> str:
    """Simulates sending a prompt to an LLM with validation and error simulation."""
    # Defensive check: Do not send empty prompts to the model!
    if len(prompt.strip()) == 0:
        raise ValueError("Prompt cannot be empty! Please provide a question.")
    
    if simulate_error:
        # Deliberately raise a ConnectionError to simulate network failure
        raise ConnectionError("AI Provider endpoint timed out (504 Gateway Timeout).")
    
    return f"AI Response: The answer to '{prompt}' is 42."

# 2. Testing with an empty prompt
user_query = "   "  # Only spaces, which .strip() reduces to empty string

try:
    print("Sending request to AI model...")
    response = call_ai_model(user_query, simulate_error=False)
    print(response)

except ValueError as ve:
    # Catches invalid user inputs locally before contacting the cloud
    print(f"\n[BAD REQUEST] Validation error: {ve}")

except ConnectionError as ce:
    # Catches network and remote server failures
    print(f"\n[ALERT] Network Error: {ce}")
    print("Action taken: Switching to backup fallback model.")

finally:
    # Always runs to clean up resources and log
    print("\n[LOG] Request cycle completed. Closing session.")