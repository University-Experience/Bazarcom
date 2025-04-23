from flask import Flask, jsonify
import requests

app = Flask(__name__)

# migrate = Migrate(app, db)
app.secret_key = '12345678'



@app.route('/gateway/books', methods=['GET'])
def get_books():
    response = requests.get('http://catalog_service:5000/catalog/books')
    if response.status_code == 200:
        books = response.json()
        return jsonify(books), 200
    else:
        return jsonify({"message" : "Error"}), 404


    
@app.route('/gateway/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    response = requests.get(f'http://catalog_service:5000/catalog/books/{book_id}')
    if response.status_code == 200:
        books = response.json()
        return jsonify(books), 200
    else:
        return jsonify({"message" : "Error"}), 404


@app.route('/gateway/books/<string:topic>', methods=['GET'])
def get_book_by_catalog(topic):
    response = requests.get(f'http://catalog_service:5000/catalog/books/{topic}')
    if response.status_code == 200:
        books = response.json()
        return jsonify(books), 200
    else:
        return jsonify({"message" : "Error"}), 404


@app.route('/gateway/purchase/<int:book_id>', methods=['POST'])
def purchase(book_id):
    response = requests.post(f'http://order_service:6000/order/purchase/{book_id}')
    print(response.json()) 
    if response.status_code == 200: 
        books = response.json()
        return jsonify(books), 200
    else:
        return jsonify({"message" : "Error on gateway"}), 404



if __name__ == '__main__':
    # Specify the port when running the Flask app
    app.run(host='0.0.0.0', port=5050)

    
