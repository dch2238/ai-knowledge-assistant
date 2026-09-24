# 1. Defining the 4 core AI variables
prompt = "Summarize the quarterly financial report."  # str
token_count = 150                                      # int
temperature = 0.7                                      # float
is_streaming = True                                    # bool

result = f"Total tokens: " + str(token_count)
print(result)

# 2. Inspecting the types using Python's built-in type() function
print(f"prompt is: {type(prompt)}")
print(f"token_count is: {type(token_count)}")
print(f"temperature is: {type(temperature)}")
print(f"is_streaming is: {type(is_streaming)}")