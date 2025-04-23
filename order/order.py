from datetime import datetime
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from sqlalchemy.orm import sessionmaker
import requests
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'order_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
# migrate = Migrate(app, db)
app.secret_key = '12345678'


# Models
class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.DateTime)

    def __init__(self, book_id, total_price, order_date):
        self.book_id = book_id
        self.total_price = total_price
        self.order_date = order_date

    def __repr__(self): 
        return f"<Order {self.id}>"


class OrderSchema(ma.Schema):
    model = Order
    fields = ('id', 'total_price', 'book_id', 'order_date')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


# with app.app_context():
#     db.drop_all()
    # db.create_all()



@app.route('/order/purchase/<int:book_id>', methods=['POST'])
def purchase(book_id):
    response = requests.post(f'http://127.0.0.1:5000/catalog/books/{book_id}/decreament')
    if response.status_code == 200:

        order_date = datetime.now()

        order = Order(book_id=book_id, total_price=response.json().get('total_price'), order_date=order_date)
        db.session.add(order)
        db.session.commit()
        return jsonify(response.json().get('message')), 200
    else:
        return jsonify({"message" : "Error on order"}), 404



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000)
