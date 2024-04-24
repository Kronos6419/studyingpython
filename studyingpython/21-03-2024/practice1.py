class Book:
    def __innit__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price 

    def getPrice(self):
        if hasattr(self, "discount"):
            return self.price - (self.price * self.discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self.discount = amount

book1 = Book("What is the color of the wind?", "Anne herbauts", 36, 39.99) 
book2 = Book("Harry Potter", "J.K Rowling", 223, 22.50)


print(book1.title)
print(book1.author)
print(book1.price)

print(book2.getPrice())
book2.setDiscount(0.25)
print(book2.getPrice())