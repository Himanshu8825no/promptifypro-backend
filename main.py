from flask import Flask, request, jsonify
from promptifypro_engine import upgrade_prompt
import os

app = Flask(__name__)

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
    return "Promptify Pro Backend is Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
