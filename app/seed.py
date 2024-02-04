from models import db, Restaurant, RestaurantPizza, Pizza
from app import app

def seed_data():
    with app.app_context():
        restaurant1 = Restaurant(name="chelsea", address="123 Main St")
        restaurant2 = Restaurant(name="star wars", address="456 Oak St")
        restaurant3 = Restaurant(name="red hut", address="101 dark web")
        restaurant4 = Restaurant(name="green garden", address="789 Elm St")
        restaurant5 = Restaurant(name="blue ocean", address="202 Pearl St")
        restaurant6 = Restaurant(name="golden dragon", address="303 Bamboo St")

        pizza4 = Pizza(name="Vegetarian", ingredients="Tomato, Bell Peppers, Mushrooms, Olives, Cheese")
        pizza5 = Pizza(name="BBQ Chicken", ingredients="BBQ Chicken, Red Onions, Cheese")
        pizza6 = Pizza(name="Hawaiian", ingredients="Ham, Pineapple, Cheese")
        pizza7 = Pizza(name="Supreme", ingredients="Pepperoni, Sausage, Mushrooms, Bell Peppers, Onions, Olives, Cheese")        
        pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")  
        pizza2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Cheese, Tomato Sauce")
        pizza3 = Pizza(name="papy", ingredients="cheese")  

        restaurant_pizzas4 = RestaurantPizza(
            restaurant=restaurant4, pizza=pizza4, price=25
        )
        restaurant_pizzas5 = RestaurantPizza(restaurant=restaurant5, pizza=pizza5, price=28)
        restaurant_pizzas6 = RestaurantPizza(restaurant=restaurant6, pizza=pizza6, price=22)
        restaurant_pizzas7 = RestaurantPizza(restaurant=restaurant1, pizza=pizza7, price=30)

        restaurant_pizzas1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=30)
        restaurant_pizzas2 = RestaurantPizza(
            restaurant=restaurant2, pizza=pizza2, price=20
        )
        restaurant_pizzas3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=10)

        db.session.add_all([restaurant4, restaurant5, restaurant6, pizza4, pizza5, pizza6, pizza7, restaurant_pizzas4, restaurant_pizzas5, restaurant_pizzas6, restaurant_pizzas7])
        db.session.commit()

if __name__ == "__main__":
    seed_data()
