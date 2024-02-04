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
    
# Delete a restaurant by ID along with associated pizzas
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Delete associated RestaurantPizza records
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204  # Empty response with status code 204 for successful deletion
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    
 # Get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = pizza_schema.dump(pizzas)
    return jsonify(result)  
# Create a new RestaurantPizza (association of Pizza and Restaurant with a price)
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id') 

    # Validate price
    if not (1 <= price <= 30):
        return jsonify({'errors': ['Validation error: Price must be between 1 and 30']}), 400


if __name__ == '__main__':
    app.run(port=5555)
