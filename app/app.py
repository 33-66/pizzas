#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Restaurant,Pizza,RestaurantPizza

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
 
@app.route('/')
def home():
    return '<ol><li>Restuarants</li><li>Pizza</li><li>add_pizza</li></ol>'
@app.route("/restaurants",methods=["GET"])
def restaurants():
    restaurants = Restaurant.query.all()
    restaurants_lists = []
    for each_restuarant in restaurants:
        restaurants_dict ={
            "id":each_restuarant.id,
            "name":each_restuarant.name,
            "address":each_restuarant.address
        }
        restaurants_lists.append(restaurants_dict)
    response = make_response(jsonify(restaurants_lists),200)
    return response
@app.route("/restaurants/<int:id>",methods = ["GET"])        
def get_restuarant(id):
    each_restuarant = Restaurant.query.get(id)
    if  each_restuarant:

        restaurants_dict = {
            "id": each_restuarant.id,
            "name": each_restuarant.name,
            "address": each_restuarant.address,
        }
        response = make_response(jsonify(restaurants_dict),200)
    else:
        response = make_response(jsonify({"error":"Restaurant not found"}),404)
        
    return response
@app.route("/restaurants/<int:id>",methods=["DELETE"])
def delete_restuarnt(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return make_response("",204)
    else:
        response = {"error":"Restaurant not found"}
        return make_response(jsonify(response),404)
@app.route("/pizzas" ,methods=["GET"])        
def pizza():
    pizzas = Pizza.query.all()
    pizza_list = []
    for each_pizza in  pizzas:
        pizza_dict = {
            "id": each_pizza.id,
            "name": each_pizza.name,
            "ingredients":each_pizza.ingredients
        }
        pizza_list.append(pizza_dict)
    response = make_response(jsonify(pizza_list),200)
    return response

@app.route("/restaurant_pizzas", methods=["POST"])
def add_pizza():
    data = request.json

    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get('restaurant_id')

    if not all([price, pizza_id, restaurant_id]):
        return jsonify({"error": "Missing parameter"}), 400
    pizza = Pizza.query.get(pizza_id)
    if not pizza or not Restaurant.query.get(restaurant_id):
        return jsonify({"error": "Invalid pizza id or restaurant id"}), 404

    new_restaurant_pizza = RestaurantPizza(
         price=price,
         pizza_id=pizza_id,
         restaurant_id=restaurant_id
        )

    db.session.add(new_restaurant_pizza)
    db.session.commit()

    # Get data related to the Pizza
    pizza_data = {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}

    response = make_response(jsonify(pizza_data), 200)
    return response

if __name__ == '__main__':
    app.run(port=5555,debug=True)
