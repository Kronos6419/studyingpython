class Library:
    bookcollection = []

    # constructor
    def __init__(self, listofBooks):
        self.bookcollection = listofBooks

    # method to show all the books
    def displayAvailableBook(self):
        if len(self.bookcollection) == 0:
            print("No Books")

        else:
            print("The books we have in the library are:")
            for book in self.bookcollection:
                print(book)

    # method to borrow book
    def borrowbook(self, user, book):
        if book in self.bookcollection:
            self.bookcollection.remove(book)

    # method to return book
    def returnbook(self, user, book):
        self.bookcollection.append(book)
        print(f"{book} is return to the library")


## TEstcase
