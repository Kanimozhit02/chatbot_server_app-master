# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
from flask import Flask, request, jsonify
from flask_cors import CORS

# Reuse chatbot brain
from CLI_Chatbot import get_chatbot_response


# ---------------------------------------------------
# Create Flask application
# ---------------------------------------------------
app = Flask(__name__)
CORS(app)   # allow React (localhost:3000) to call this API


# ---------------------------------------------------
# API Route for Chatbot
# ---------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat():
    # get data from React
    data = request.get_json()

    # message typed by user
    user_message = data.get("message")

    # provider (openai / gemini / etc)
    # if not sent -> default openai
    provider = data.get("provider", "openai")

    # get reply from chatbot logic
    reply = get_chatbot_response(user_message, provider)

    # send response back
    return jsonify({
        "response": reply
    })


# ---------------------------------------------------
# Run Flask server
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
