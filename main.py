from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/nexus/chat', methods=['POST'])
def chat():
    data = request.json
    # process data here
    response = {"reply": "Got your message"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
