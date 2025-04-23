from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/frontend', methods=['GET'])
def index():
    return jsonify("Hello, World!")

@app.route('/frontend/books', methods=['GET'])
def get_books():
    response = requests.get(f"http://gateway_service:5050/gateway/books")
    
    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6050)