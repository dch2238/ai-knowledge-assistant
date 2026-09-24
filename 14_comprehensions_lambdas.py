# 1. Raw document chunks with messy whitespace and some useless short chunks
raw_chunks = [
    "   Antigravity platform overview.   \n",
    " hi ",  # Too short to be useful
    "   Vector embeddings transform words into mathematical vectors.   ",
    "ok",    # Too short
    "   LangGraph manages state and loops across multi-agent graphs.   "
]

queries = ["What is RAG?", "How to use TOOLS?", "WHERE IS THE DOCUMENTATION?"]

lower_queries = [q.lower() for q in queries]  # List comprehension to lowercase all queries

# 2. List Comprehension: Clean whitespace AND filter out short chunks in 1 line!
# Syntax: [transform(item) for item in list if condition]
clean_chunks = [c.strip() for c in raw_chunks if len(c.strip()) > 10]

print("--- 1. BATCH CLEANED CHUNKS ---")
for chunk in clean_chunks:
    print(f"- {chunk}")

# 3. Sorting search results with a LAMBDA function
# Imagine our vector database retrieved these 3 chunks with similarity scores:
search_results = [
    {"doc": "Doc A: General Introduction", "similarity": 0.72},
    {"doc": "Doc B: Deep Technical Spec", "similarity": 0.94},
    {"doc": "Doc C: FAQ and Troubleshooting", "similarity": 0.81}
]

# A lambda is a quick anonymous function: lambda x: x["similarity"]
# Sorts the list in-place from highest score to lowest (reverse=True)
search_results.sort(key=lambda item: item["similarity"], reverse=True)

print("\n--- 2. RANKED SEARCH RESULTS (HIGHEST TO LOWEST) ---")
for result in search_results:
    print(f"Score: {result['similarity']} | {result['doc']}")

    print(lower_queries)