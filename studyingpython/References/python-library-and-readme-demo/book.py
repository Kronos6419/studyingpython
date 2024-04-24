class Book:
    book_id = 0000
    book_title = None
    book_status = None

    # constructor
    def __init__(self, bookid, title, status=True):
        self.book_id = bookid
        self.book_title = title
        self.book_status = status

    # method
    def displayBookDetails(self):
        print("Book" + self.book_id)
        print("Title" + self.book_title)
        print("Status" + self.book_status)


# Test case
