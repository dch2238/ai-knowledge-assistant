import json

# 1. Simulating a raw JSON string returned by an LLM
raw_llm_response = '{"topic": "Quantum Computing", "sentiment": "positive", "confidence": 0.94}'
broken_llm_output = '{"topic": "Artificial Intelligence", "status": "processing"'



print("--- 1. PARSING LLM JSON RESPONSE ---")
try:
    # json.loads converts a JSON string into a usable Python dictionary
    parsed_data = json.loads(raw_llm_response)

    
    print(f"Topic: {parsed_data['topic']}")
    print(f"Sentiment: {parsed_data['sentiment']}")
    print(f"Confidence: {parsed_data['confidence'] * 100:.1f}%")

except json.JSONDecodeError as e:
    print(f"[ERROR] LLM returned invalid JSON: {e}")

# 2. Packaging an API request payload (Dictionary -> JSON string)
api_payload = {
    "model": "gpt-4o-mini",
    "temperature": 0.2,
    "messages": [
        {"role": "system", "content": "You are a financial entity extractor."},
        {"role": "user", "content": "Apple reported $90B in revenue."}
    ]
}

# json.dumps converts dictionary to a JSON string. indent=2 makes it readable
json_string = json.dumps(api_payload, indent=2)

print("\n--- 3. HANDLING BROKEN JSON ---")
try:
    data = json.loads(broken_llm_output)
except json.JSONDecodeError as e:
    print(f"[ALERT] Handled malformed JSON from model: {e}")

print("\n--- 2. SERIALIZED JSON PAYLOAD FOR API ---")
print(json_string)