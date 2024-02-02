from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'Restaurants'
# add any models you may need. 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.Integer)
    ingridients = db.Column(db.String)
class RestaurantPizza(db.Model):
    __tablename__ =  "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    price  = db.Column(db.Integer)    
