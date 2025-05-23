from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    print("Received:", data)

    # Example response
    return jsonify({
        "status": "success",
        "received": data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
