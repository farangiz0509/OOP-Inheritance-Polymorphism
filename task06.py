class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")

class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print(f"Ishlab chiqaruvchi: {self.name}, Maoshi: ${self.salary}, Bonus: ${bonus}")

class Manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.20
        print(f"Menjer: {self.name}, Maoshi: ${self.salary}, Bonus: ${bonus}")


developer = Developer("Azimbek", 20000000)
manager = Manager("Sevara", 17000000) 

developer.calculate_bonus()
manager.calculate_bonus()