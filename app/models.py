from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'Restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant")

class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)  
    ingredients = db.Column(db.String)  
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    price = db.Column(db.Integer)
    
    @validates('price')
    def validate_price(self, key, price):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return price
