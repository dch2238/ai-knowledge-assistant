from pathlib import Path

# 1. Setting up a cross-platform folder path
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  # Creates the folder if it does not exist
missing_file = data_dir / "missing_file.txt"
if not missing_file.exists():
    print(f"Warning: The file {missing_file} does not exist. Please check the path.")

doc_path = data_dir / "ai_policy.txt"
log_path = data_dir / "chat_logs.txt"

# 2. Writing a document to disk ('w' mode = write/overwrite)
policy_text = """ AI Usage Policy:
1. Always protect user data and API keys.
2. Never store passwords in prompt templates.
3. Verify retrieved chunks before passing to LLM."""

with open(doc_path, "w", encoding="utf-8") as f:
    f.write(policy_text)

print(f">> Successfully created document: {doc_path}")

# 3. Reading the document from disk ('r' mode = read)
with open(doc_path, "r", encoding="utf-8") as f:
    loaded_content = f.read()

print("\n--- LOADED DOCUMENT CONTENT ---")
print(loaded_content)

# 4. Appending to a log file ('a' mode = append)
with open(log_path, "a", encoding="utf-8") as f:
    f.write("Log Entry: Policy document was read into memory.\n")

print(f"\n>> Audit log appended to: {log_path}")