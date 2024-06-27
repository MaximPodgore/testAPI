import os
import requests
from dotenv import load_dotenv

# Load the endpoints and key from the .env file
load_dotenv()
ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
print(ENDPOINT, API_KEY)
# Define the prompt
prompt = "Hello, how can I assist you today?"

# Send the prompt to ChatGPT
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "prompt": prompt,
    "max_tokens": 100
}

response = requests.post(ENDPOINT, headers=headers, json=data)
response_json = response.json()

# Process the response
if "choices" in response_json:
    choices = response_json["choices"]
    for choice in choices:
        print(choice["text"])
else:
    print(response_json)
    print("Error: Failed to get a response from ChatGPT")