from models import db, Restaurant, RestaurantPizza, Pizza
from app import app

def seed_data():
    with app.app_context():
        restaurant1 = Restaurant(name="chelsea", address="123 Main St")
        restaurant2 = Restaurant(name="star wars", address="456 Oak St")
        restaurant3 = Restaurant(name="red hut", address="101 dark web")
        
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")  
        pizza2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Cheese, Tomato Sauce")
        pizza3 = Pizza(name="papy", ingredients="cheese")  
        
        restaurant_pizzas1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=30)
        restaurant_pizzas2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=20)
        restaurant_pizzas3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=10)
        
        db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, restaurant_pizzas1, restaurant_pizzas2, restaurant_pizzas3])
        db.session.commit()

if __name__ == "__main__":
    seed_data()
