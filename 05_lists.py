# 1. A list of retrieved document chunks from a vector database
retrieved_chunks = [
    "Chunk 1: Antigravity is an AI development platform.",
    "Chunk 2: Python 3.12 provides enhanced speed and typing.",
    "Chunk 3: RAG stands for Retrieval-Augmented Generation.",
    "Chunk 4: Vector databases store high-dimensional embeddings."
]

# 2. How many chunks do we have?
print(f"Total chunks retrieved: {len(retrieved_chunks)}")

# 3. Accessing by Index (Python is 0-indexed!)
first_chunk = retrieved_chunks[0]
latest_chunk = retrieved_chunks[-1]  # -1 always grabs the very last item

print(f"\nFirst Chunk: {first_chunk}")
print(f"Last Chunk: {latest_chunk}")

# 4. Slicing: Grab only Top-2 chunks to save tokens
top_2_chunks = retrieved_chunks[:2]
print(f"\nTop 2 Chunks for LLM Context: {top_2_chunks}")

# 5. Dynamically appending a new chunk
new_chunk = "Chunk 5: AI Agents can use tools and make autonomous decisions."
retrieved_chunks.append(new_chunk)
print(f"\nUpdated Total Chunks: {len(retrieved_chunks)}")

# A mock 3-dimensional vector embedding representing a word
word_vector = [0.42, -0.88, 0.15]
word_vector.append(0.99)  # Adding a new dimension to the vector
print(f"\nWord Vector with New Dimension: {word_vector}")