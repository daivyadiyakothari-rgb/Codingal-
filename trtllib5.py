# Activity 1 (Class Student)
class student:
  grade = 10
  print("Hi, I am student of grade", grade)

ob = student()

# Activity 2 (Class Student 2)
class stdent: 
  grade = 10
  name = "Penguin"

  def introduction(self):
    print("Hi, I am", self.name)
    print("I am student of grade", self.grade)

ob = student()    
ob.intorduction()
ob.details()

# Activity 3 (Parrot Bird)
class Parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        print("I am a", self.species)
        print("My name is", self.name)
        print("I am", self.age, "years old")

blue = Parrot("Blue", 10)
Woo = Parrot("Woo", 15)

print("Blue is a {}".format(blue.species))
print("Woo is a {}".format(Woo.species))

# Acctivity 4 (Parrot Bird 2)
class Parrot:
   def __init__(self, name, age):
         self.name = name
         self.age = age
   def sing(self, song):
            return "{} sings {}".format(self.name,song)
   def dance(self):
       return "{} is now dancing".format(self.name)
blue = Parrot("Blue", 10)

print(blue.sing("Happy"))
print(blue.dance())