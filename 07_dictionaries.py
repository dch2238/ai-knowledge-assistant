# 1. An AI Document Chunk with structured metadata
chunk_record = {
    "chunk_id": "doc_402_chunk_1",
    "text": "Antigravity supports multi-agent systems and MCP protocols.",
    "page": 14,
    "source_file": "architecture_guide.pdf"
}

# 2. Accessing data using keys (Square Bracket syntax)
print(f"Chunk ID: {chunk_record['chunk_id']}")
print(f"From File: {chunk_record['source_file']} (Page {chunk_record['page']})")

# 3. Defensive coding with .get() (Avoids crashing!)
# If the key 'author' doesn't exist, return 'Anonymous' instead of crashing
author = chunk_record.get("author", "Anonymous")
print(f"Author: {author}")

# 4. Modifying and Adding new keys dynamically
chunk_record["token_count"] = 12
chunk_record["is_embedded"] = True

print(f"\nUpdated Chunk Record:")
print(chunk_record)

chat_history = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Explain Python dictionaries."},
    {"role": "assistant", "content": "Dictionaries store key-value pairs."}
]

chat_history.append({"role": "user", "content": "How do I add a new key-value pair?"})
print(f"\nUpdated Chat History:")
for message in chat_history:
    print(f"{message['role'].capitalize()}: {message['content']}")