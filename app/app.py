#!/usr/bin/env python3

from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/simon/Flask/code_challenge2/python-code-challenge-pizzas/python-code-challenge-pizzas/code-challenge/app/db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>restaurants</h1>'
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
        
    pass


if __name__ == '__main__':
    app.run(port=5555,debug=True)
