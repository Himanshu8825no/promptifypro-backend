from flask import Flask, request, jsonify
from promptifypro_engine import upgrade_prompt
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    basic_prompt = data.get("prompt", "")
    if not basic_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    upgraded = upgrade_prompt(basic_prompt)
    return jsonify({"upgraded_prompt": upgraded})

@app.route("/")
def home():
    return "Promptify Pro Backend is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
