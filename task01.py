class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")


class Dog(Animal):
    def speak(self):
        return f"{self.name} Vov-vov!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} Miyavv!"
    
dog = Dog("Bingo")
cat = Cat("Bagira")

print(dog.speak())
print(cat.speak())