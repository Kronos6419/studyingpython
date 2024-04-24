class User:
    user_id = 2000
    user_name = None
    listofbook = []

    # Constructor
    def __init__(self, name):
        self.user_name = name
        self.listofbook = []

    # method
    def accountDetails(self):
        print("================== Account Info ==================")

        print("Name: " + self.user_name)
        print("Borrowed book: ")
        for book in self.listofbook:
            print(book)

    def addBook(self, book):
        self.listofbook.append(book)

    def removeBook(self, book):
        self.listofbook.remove(book)
