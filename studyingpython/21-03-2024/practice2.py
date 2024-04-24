class Cat:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print("Meow")

    def displayInfo(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        
class DomesticatedCat(Cat):

    def __init__(self, name, age, owner, homeAddress):
        super().__init__(name, age)
        self.owner = owner
        self.homeAddress = homeAddress

    def displayInfo(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Owner: {self.owner}')
        print(f'Address: {self.homeAddress}')

class WildCat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.flies = True

    def checkForFlies(self):
        if self.flies : True 
        print("Has Flies")
    

#creating instance of object
cat1 = Cat("Doug", 5)


#calling class methods
cat1.sound()
cat1.displayInfo()

cat2 = ("Bob", 3, 'Hermant', '1 Boo St')
cat2.displayInfo()