from openai import OpenAI

# Initialize the OpenAI client with the API key (enclosed in double quotes)
client = OpenAI(
    api_key=
)
# Your conversation or command content
command = "Hello, how can I help you today?"

# Calling OpenAI API to generate a response
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named unais skilled in general tasks like Aleva and Google Cloud"},
        {"role": "user", "content": command}
    ]
)

# Print the completion result
print(completion.choices[0].message.content)
