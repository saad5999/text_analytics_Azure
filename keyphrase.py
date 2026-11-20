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

question = input ("Give me the content...\n");

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are an ai assistant who only extracts the key phrases in the provided content by user"},
        {"role": "user", "content": question}
    ],
)

print(f"\n\nanswer: {response.choices[0].message.content}")