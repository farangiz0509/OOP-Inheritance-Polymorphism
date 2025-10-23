import math


class Shape:
    def info(self):
        print("Shape")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2
        

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b 


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) /2
        return (p*(p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    

circle = Circle(7)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)


print("Doira yuzi:", circle.area())
print("To'rtburchak:", rectangle.area())
print("Uchburchak yuzi:", triangle.area())