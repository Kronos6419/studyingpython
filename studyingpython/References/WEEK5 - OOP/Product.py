# class Product
from math import isnan
class Product:
    name = None
    price = None
    quantity = None
    weight = None

    # constructor
    def __init__(self, name, price, quantity, weight):
        self.name = name
        self.price = round(price, 2)
        self.quantity = quantity
        self.weight = weight


    # display all attributes
    def display(self):
        print("\n******* PRODUCT *********")
        print("name:", self.name)
        print(f"price: ${self.price}" )
        print("quantity:", self.quantity)
        print(f"cost: ${self.cost()}")
        print("weight:", self.weight, "\n")



    # get price
    def get_price(self):
        return self.price
    

    # set a new price
    # parameter: new price
    def set_price(self, new_price):
        # if price is NOT A NUMBER
        if isnan(new_price):
            return False
        
        if new_price < 0:
            return False
        
        self.price = round(new_price, 2)
        return True


    # get a quantity value
    def get_quantity(self):
        return self.quantity


    # set a quantity
    # parameter: new_quantity
    def set_quantity(self, new_quantity):
        # if new_quantity is NOT A NUMBER
        if isnan(new_quantity):
            return False
        
        if new_quantity < 0:
            return False
        
        self.quantity = new_quantity
        return True
    

    # sell several items
    # parameter sold_quantity - the number of items to sell
    def sell(self, quantity_to_sell):
        # if sold_quantity is NOT A NUMBER
        if isnan(quantity_to_sell):
            return False
        
        if quantity_to_sell < 0 or quantity_to_sell > self.quantity:
            return False
        
        self.quantity -= quantity_to_sell
        return True
        

    # calculates the cost of the product in stock
    # and rounds to two decimal places
    def cost(self):
        return round(self.quantity * self.price, 2)

        

    
