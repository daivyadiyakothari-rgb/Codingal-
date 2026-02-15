# Activity 1 (Inheritance)
class Vehical:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehical):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# Activity 2 
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)
a = Employee("Rahul", 886012, 200000, "Intern")
a.display()
# After class project 
from abc import ABC, abstractmethod
import math


class Polygon(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def show_area(self):
        print(f"{self.name} Area = {self.area():.2f}")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RegularPolygon(Polygon):
    def __init__(self, sides, length):
        super().__init__("Regular Polygon")
        self.sides = sides
        self.length = length

    def area(self):
        return (self.sides * self.length ** 2) / (4 * math.tan(math.pi / self.sides))


def main():
    shapes = []

    # Hardcoded sample data
    shapes.append(Rectangle(10, 5))
    shapes.append(Square(4))
    shapes.append(Triangle(6, 8))
    shapes.append(RegularPolygon(5, 3))

    for shape in shapes:
        shape.show_area()


if __name__ == "__main__":
    main()

