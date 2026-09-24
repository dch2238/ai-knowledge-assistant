# 1. A reusable function to calculate token costs
def calculate_cost(tokens: int, price_per_thousand: float = 0.002) -> float:
    """Calculates API cost given token count and price per 1k tokens."""
    cost = (tokens / 1000) * price_per_thousand
    return cost

# 2. A reusable prompt builder function
def build_rag_prompt(system_role: str, context: str, user_question: str) -> str:
    """Combines system instructions, retrieved context, and the user question."""
    prompt = f"""SYSTEM: {system_role}
CONTEXT:
{context}

USER QUESTION: {user_question}
ANSWER:"""
    return prompt

# 3. Calling the functions
doc_context = "AI supports LangGraph and MCP."
question = "What frameworks does AI support?"

final_prompt = build_rag_prompt(
    system_role="You are a factual AI assistant.",
    context=doc_context,
    user_question=question
)

prompt1 = "What is the weather today?"

estimated_cost = calculate_cost(tokens=450)

# 4. Display results
print("--- GENERATED PROMPT ---")
print(final_prompt)
print(f"\nEstimated Cost: ${estimated_cost:.6f}")

def is_prompt_safe(prompt: str) -> bool:
    """Checks if the prompt contains any unsafe content."""
    # Placeholder logic - replace with actual safety checks
    unsafe_keywords = ["unsafe", "harmful", "dangerous"]
    for keyword in unsafe_keywords:
        if keyword in prompt.lower():
            return False
    return True

# Unindented back to the left margin:
test_prompt = "What is the weather today?"
result = is_prompt_safe(test_prompt)

print(f"\nIs the prompt safe? {'Yes' if result else 'No'}")