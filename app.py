from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route("/", methods=["POST"])
def zapier_webhook():
    data = request.json
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
