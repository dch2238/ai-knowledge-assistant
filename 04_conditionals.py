# 1. Similarity score from Vector Database (scale: 0.0 to 1.0)
similarity_score = 0.25
token_count = 600
MAX_CHUNK_TOKENS = 200

# 2. Conditional Gatekeeper
if similarity_score >= 0.80 and token_count <= MAX_CHUNK_TOKENS:
    decision = "ACCEPT: High quality chunk, fits in context window."
elif similarity_score >= 0.60:
    decision = "REVIEW: Moderate quality chunk, consider secondary search."
else:
    decision = "REJECT: Low relevance chunk, do not send to LLM."

# 3. Print the decision
print(f"Similarity Score: {similarity_score}")
print(f"Gatekeeper Decision: {decision}")