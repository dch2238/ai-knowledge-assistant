# Part 1: Assembling Prompt Context with a FOR loop
retrieved_chunks = [
    "Python is an interpreted, high-level programming language.",
    "RAG retrieves relevant context to reduce hallucinations.",
    "Vectors represent the semantic meaning of text."
]

assembled_context = ""

# enumerate() gives us BOTH the index (0, 1, 2) and the chunk text
for i, chunk in enumerate(retrieved_chunks):
    assembled_context += f"[Doc {i + 1}] {chunk}\n"

print("--- ASSEMBLED CONTEXT FOR LLM ---")
print(assembled_context)

# Part 2: AI API Retry mechanism with a WHILE loop
attempts = 0
max_retries = 3
api_connected = False

print("--- ATTEMPTING API CONNECTION ---")
while not api_connected and attempts < max_retries:
    attempts += 1
    print(f"Connecting to AI Model... (Attempt {attempts} of {max_retries})")
    
    # Simulate success on attempt 2
    if attempts == 2:
        api_connected = True
        print(">> Connection Successful!")


        total_words = 0
        for chunk in retrieved_chunks:
            total_words += len(chunk.split())
            print(f"Chunk: '{chunk}' | Word Count: {len(chunk.split())}")

        print(f"\nTotal Words in Context: {total_words}")