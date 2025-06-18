from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# OpenRouter settings
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-4o"

def upgrade_prompt(basic_prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a world-class prompt engineer. You will take any basic prompt and rewrite it into a highly detailed, professional-level prompt to get the best result."},
            {"role": "user", "content": basic_prompt}
        ]
    }

    response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        upgraded_prompt = response.json()["choices"][0]["message"]["content"]
        return upgraded_prompt
    else:
        raise Exception(f"OpenRouter API error: {response.text}")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    basic_prompt = data.get("prompt", "")
    if not basic_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        upgraded_prompt = upgrade_prompt(basic_prompt)
        return jsonify({"upgraded_prompt": upgraded_prompt})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Promptify Pro Backend is Running with OpenRouter!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
