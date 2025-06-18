import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def upgrade_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional prompt engineer. Improve the following prompt to make it highly effective, creative, and specific."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']
