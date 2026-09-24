# 1. Model specifications (GPT-4o / Claude / Gemini style)
CONTEXT_WINDOW = 128000                  # Maximum tokens allowed (int)
PRICE_PER_1K_INPUT_TOKENS = 0.0025       # $0.0025 per 1,000 tokens (float)
PRICE_PER_1K_OUTPUT_TOKENS = 0.0100      # $0.0100 per 1,000 tokens (float)

# 2. Token counts for a specific chat message
input_tokens = 3500
output_tokens = 800
doc_words = 10500  # Total words in the document

# chunks
full_chunks = doc_words // 800
leftover_words = doc_words % 800

# 3. Cost calculation
input_cost = (input_tokens / 1000) * PRICE_PER_1K_INPUT_TOKENS
output_cost = (output_tokens / 1000) * PRICE_PER_1K_OUTPUT_TOKENS
total_cost = input_cost + output_cost

# 4. Remaining context calculation
total_tokens_used = input_tokens + output_tokens
tokens_remaining = CONTEXT_WINDOW - total_tokens_used

# 5. Display the results
print(f"Total Tokens Used: {total_tokens_used}")
print(f"Tokens Remaining: {tokens_remaining}")
print(f"Total API Cost: ${total_cost:.5f}")
print(f"Full Chunks: {full_chunks}")
print(f"Leftover Words: {leftover_words}")