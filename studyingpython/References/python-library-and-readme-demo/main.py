from library import Library
from user import User

communityLibrary = Library(["Book 1", "Book 2", "Book 3"])
members = [User("Jerry"), User("Tom")]


def findUser(name):
    for member in members:
        if member.user_name == name:
            return member
    return None


def main():
    print("==== Menu ====")
    print("1. Show all available books")
    print("2. Borrow a book")
    print("3. return a book")
    print("4. Check your account")
    print("5. Exit")
    print("==============")

    while True:
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            print("Books currently available are: ")
            communityLibrary.displayAvailableBook()

            # print everything
        elif user_choice == "2":
            print("To borrow book")
            request = input("Which book you are borrowing?")
            borrower = input("What is your name? ")
            user = findUser(borrower)
            communityLibrary.borrowbook(user, request)
        elif user_choice == "3":
            print("To return book")
            returnbook = input("Which book you are borrowing?")
            borrower = input("What is your name? ")
            user = findUser(borrower)
            communityLibrary.borrowbook(user, returnbook)
        elif user_choice == "4":
            userProfile = input("Enter username: ")
            user = findUser(userProfile)
            user.accountDetails()
        elif user_choice == "5":
            exit()


if __name__ == "__main__":
    main()
