# EXERCISE 8-1 INHERITANCE
# Product for online-shop

# parent class
class Product():
    name: None
    __price: None
    quantity: None

    # constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    # dipslay product's info
    def display(self):
        print("\n***** PRODUCT *****")
        print("name:", self.name)
        print("quantity:", self.quantity)
        print("price:", self.__price)

    # calculates the total cost
    def calculate_total(self):
        return self.__price * self.quantity
    
    # getter: get price
    def get_price(self):
        return self.__price
    
    # setter: get price
    def set_price(self, new_price):
        self.__price = new_price
    


# child classes
# class ELECTRONICS
class Electronics(Product):
    brand: None

    # constructor
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)

        self.brand = brand

    # re-define the display function to display more info
    # polymorphism
    def display(self):
        super().display()

        print("section: ELECTRONICS")
        print("brand: ", self.brand)



# class CLOTHING
class Clothing(Product):
    size: None

    # constructor
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)

        self.size = size

    # re-define the display function to display more info
    # polymorphism
    def display(self):
        super().display()

        print("section: CLOTHING")
        print("size: ", self.size)


# class BOOK
class Book(Product):
    author: None

    # constructor
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)

        self.author = author

    # re-define the display function to display more info
    # polymorphism
    def display(self):
        super().display()

        print("section: BOOKS")
        print("author: ", self.author)
    