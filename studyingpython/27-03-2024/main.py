#To import from another file (CASE SENSITIVE)
from person import Person

#Main Function that'll define subsequent classes
def main():
    print("Hello, User!")
    name = input("What is your name?")
    person = Person(name)
    person.greet()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, {self.name}!")

#main() would only run in the same file, the rest of the code is to run the whole code.
if __name__ == "__main__":
    main()