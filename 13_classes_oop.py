# 1. Defining the DocumentChunk Blueprint (Class)
class DocumentChunk:
    def __init__(self, chunk_id: str, text: str, page: int, source_file: str):
        """The Constructor: Initializes a new chunk whenever one is created."""
        self.chunk_id = chunk_id
        self.text = text
        self.page = page
        self.source_file = source_file

    def get_word_count(self) -> int:
        """A method to count the words in this specific chunk."""
        return len(self.text.split())

    def format_citation(self) -> str:
        """Formats a clean citation reference for the LLM answer."""
        return f"[{self.source_file} | Page {self.page}]"

    def is_too_long(self, max_words: int = 10) -> bool:
        """Checks if the chunk exceeds a specified word limit."""
        return self.get_word_count() > max_words

# 2. Creating (Instantiating) two distinct chunk objects
chunk1 = DocumentChunk(
    chunk_id="chk_001",
    text="Antigravity uses high-dimensional vector embeddings for RAG retrieval.",
    page=3,
    source_file="architecture_spec.pdf"
)

chunk2 = DocumentChunk(
    chunk_id="chk_002",
    text="LangGraph enables cyclic state machines for multi-agent workflows.",
    page=15,
    source_file="agents_handbook.pdf"
)

# 3. Interacting with the objects
print(f"Chunk 1 ID: {chunk1.chunk_id}")
print(f"Chunk 1 Citation: {chunk1.format_citation()}")
print(f"Chunk 1 Word Count: {chunk1.get_word_count()} words")

print(f"\nChunk 2 Citation: {chunk2.format_citation()}")
print(f"Chunk 2 Word Count: {chunk2.get_word_count()} words")
print(f"Is Chunk 1 too long? {'Yes' if chunk1.is_too_long(max_words=5) else 'No'}")