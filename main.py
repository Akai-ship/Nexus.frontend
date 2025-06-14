from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/nexus/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data['message']
    reply = f"Echo: {user_message}"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
curl -X POST http://localhost:5000/nexus/chat -H "Content-Type: application/json" -d '{"message":"hello"}'
