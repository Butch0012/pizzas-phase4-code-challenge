#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Routes

# Get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = restaurant_schema.dump(restaurants)
    return jsonify(result)

# Get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        result = restaurant_schema.dump(restaurant)
        return jsonify(result)
    else:
        return jsonify({'error': 'Restaurant not found'}), 404


if __name__ == '__main__':
    app.run(port=5555)
