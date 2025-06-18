import openai

client = openai.OpenAI()

def upgrade_prompt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a professional prompt engineer. Upgrade this prompt to make it highly effective."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    upgraded_prompt = response.choices[0].message.content
    return upgraded_prompt
