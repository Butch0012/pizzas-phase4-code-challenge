from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'Restaurant'

    id = db.Column(db.Integer, primary_key=True)

# add any models you may need. 
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Restaurant name
    address = db.Column(db.String(100), nullable=False)  # Restaurant address
    pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)  # Relationship with RestaurantPizza model

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)  # Pizza name
    ingredients = db.Column(db.String(200), nullable=False)  # Pizza ingredients
    restaurants = db.relationship('RestaurantPizza', backref='pizza', lazy=True)  # Relationship with RestaurantPizza model