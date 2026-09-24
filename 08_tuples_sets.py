# 1. TUPLE: Immutable fixed configuration (parentheses)
# An image resolution passed to a Vision AI model (Width, Height, Channels)
image_dimensions = (1920, 1080, 3)

print(f"Image Resolution: {image_dimensions[0]}x{image_dimensions[1]}")
# image_dimensions[0] = 1280  <-- This would CRASH! Tuples cannot be modified.

# 2. SET: Automatic Deduplication for Search Results
# Imagine these 5 chunk IDs were returned from hybrid search (notice duplicates!)
raw_retrieved_ids = ["chunk_A", "chunk_B", "chunk_A", "chunk_C", "chunk_B"]

print(f"\nRaw search results (with duplicates): {raw_retrieved_ids}")
print(f"Total count before deduplication: {len(raw_retrieved_ids)}")

# Convert list to set to wipe out duplicates
unique_ids = set(raw_retrieved_ids)

print(f"Deduplicated unique IDs (Set): {unique_ids}")
print(f"Unique count: {len(unique_ids)}")

unique_ids.add("chunk_D")  # Adding a new unique chunk ID
print(f"\nUpdated Unique IDs (after adding chunk_D): {unique_ids}")