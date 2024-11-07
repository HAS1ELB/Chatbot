# main.py

from flask import Flask, request, jsonify
from bot_logic import generate_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    
    if not user_input:
        return jsonify({"error": "Aucun message reçu."}), 400
    
    bot_response = generate_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
