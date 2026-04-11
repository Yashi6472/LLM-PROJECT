from openai import OpenAI

message = "Hello, GPT! Can you tell me 10 good things about NAGPUR City in Maharashtra."

messages = [{"role": "user", "content": message}]

print(messages)

OLLAMA_BASE_URL="http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content": message}])
print(response.choices[0].message.content)