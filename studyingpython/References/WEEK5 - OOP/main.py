from Product import Product

if __name__ == "__main__":

    product1 = Product("Ginger cookies", 12.00, 12, "100g")
    product1.display()

    print(product1.sell(3))
    print(product1.get_quantity())

    print(product1.sell(20))
    print(product1.get_quantity())

    print(product1.set_price(10.99))
    print(product1.get_price())

    product1.display()
