import time
import requests
from langchain_huggingface import HuggingFaceEndpoint

endpoint_url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
api_key = "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"

llm = HuggingFaceEndpoint(endpoint_url=endpoint_url, api_key=api_key)

def generate_response_with_retry(prompt, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = llm.generate(prompts=[prompt])
            return response
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Too many requests
                print("Rate limit hit. Retrying...")
                time.sleep(delay)
            else:
                raise e
    return "Failed after retries"

prompt = "Your prompt here"
response = generate_response_with_retry(prompt)
print(response)
