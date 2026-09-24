# 1. Multi-line System Prompt using triple quotes """
system_prompt = """You are a helpful AI Assistant.
Always answer truthfully.
If you do not know the answer, say 'I do not know'."""

# 2. Raw, messy user input from a web form
raw_user_input = "   What is the capital of France?   \n"

# 3. Clean the text using .strip()
cleaned_input = raw_user_input.strip()

modifed_input = cleaned_input.replace("France", "Germany")

# 4. Measure character length using len()
char_count = len(cleaned_input)

# 5. String Slicing (taking the first 15 characters only)
preview = cleaned_input[:15]

# 6. Display results
print(f"Cleaned Input: '{cleaned_input}'")
print(f"Modified Input: '{modifed_input}'")
print(f"Total Characters: {char_count}")
print(f"First 15 Characters: '{preview}...'")