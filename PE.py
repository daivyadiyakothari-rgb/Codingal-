# Activity 1: Polymorphism Implementation
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} is {self.age} years old.")

    def make_sound(self):
        print("Meow!")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"{self.name} is {self.age} years old.")

    def make_sound(self):
        print("Woof!")
cat1 = Cat("Dodo", 2.5)
dog1 = Dog("Rex", 3)

for animal in [cat1, dog1]:
    animal.info()
    animal.make_sound()

# Activity 2: Encapsulation Implementation
class Computor:
    def __init__ (self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computor()
c.sell()

# Change the price
c.setMaxPrice(1000)
c.sell()

# Using setter function
c.setMaxPrice(1000)
c.sell()