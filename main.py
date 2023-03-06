import os
import openai

openai.organization = "org-m8H93TRE4NVFfjSmsDKOt7pT"
openai.api_key = os.getenv('OPENAI_API_KEY')

print("Let's have a chat with Openai ....")
prompt = input('> ')

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=3000,
)

print(response.choices[0].text)