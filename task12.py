class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_dashboard(self):
        raise NotImplementedError("Bunday metod mavjud emas! ")


class Student(User):
    def get_dashboard(self):
        print(f"Familyasi:{self.first_name} Ismi:{self.last_name} Yoshi:{self.age}")

class Instructor(User):
    def get_dashboard(self):
        print(f"Familyasi:{self.first_name} Ismi:{self.last_name} Yoshi:{self.age}")


student = Student("Latipova", "Sevara", 20)
instructor = Instructor("Qodirov", "Asliddin", 30)

student.get_dashboard()
instructor.get_dashboard()