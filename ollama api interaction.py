import requests

url = "http://localhost:11434/api/generate"
payload = {
    "model" : "llama3.2",
    "prompt" : "Tell me 5 Good Things about Contraversiesial Topics.",
    "stream" : False
}
response = requests.post(url,json= payload)
print(response.json()["response"])