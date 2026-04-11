from openai import OpenAI

sys_prompt = f"""You are a helpful assistant that 
summarizes the content of a website 
in simple understandable terms."""

user_prompt = f"""Please summarize the content of the 
given website and provide all information in bullet 
points, starting with the highest priority information."""

def messages_for(website):
    return [
        {"role":"system", "content": sys_prompt},
        {"role":"user","content":user_prompt+website}
    ]

OLLAMA_BASE_URL="http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=messages_for("https://www.lifewire.com/open-task-manager-in-windows-10-5191172"))
print(response.choices[0].message.content)