from openai import AzureOpenAI

deployment_name = "gpt-5-mini"
# Use the alternative standard Azure OpenAI resource endpoint and key from cell qh-BHZ7lOvyX
endpoint_clean = ""
api_key_clean = ""
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=endpoint_clean,
    api_key=api_key_clean,
    api_version="2024-08-01-preview",
)

user_prompt = input ("Give me the content...\n");

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are an AI Assistant who analyses the sentiment of the user content and retruns the result in one word."},
        {"role": "user", "content": user_prompt}
    ],
)

print(f"\n\nanswer: {response.choices[0].message.content}")