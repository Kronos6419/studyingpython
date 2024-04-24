#Class Example

class Person:
    # constructor (constructs attributes)
    def __init__(self, name, age, hairColor, eyeColor):
        self.name = name
        self.age = age
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.hasBeard = True

    #method
    def speaks(self):    
        quote = input(f"what does {self.name} say?: ")
        print(f"{self.name} says: ", quote)

    #method with a parameter (years)
    def gets_older(self, years):
        self.age += years 
        print(f"{self.name} is now {self.age}")   

    def isHairy(self):
        if self.hasBeard == True:
            print(f"{self.name} has a cool beard.") 
        else:
            print(f"{self.name} has a cool chin.")  

    #method to change hair color
    def change_hair_color(self, new_color):
        self.hairColor = new_color
        print(f"{self.name} changed hair color to {self.hairColor}")

    #method to change eye color
    def change_eye_color(self, new_color):
        self.eyeColor = new_color
        print(f"{self.name} changed eye color to {self.eyeColor}")
    

cindy = Person("Cindy Shaw", 45, "blonde", "brown")   
henry = Person("Henry Shaw", 34, "brown", "blue")

#cindy.speaks()
henry.gets_older(6)
henry.isHairy()
print(cindy.name)
print(henry.age)
cindy.change_hair_color("red")
henry.change_eye_color("green")