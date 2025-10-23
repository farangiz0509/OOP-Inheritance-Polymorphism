class User():
    def __init__(self, first_name, last_name, year):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
    
    def access_level(self):
        raise NotImplementedError("Bunday metod mavjud emas!")
    

class Admin(User):
    def access_level(self):
        print(f"Admin kirish huquqi: {self.first_name} {self.last_name} {self.year} - hamma tizimga kirishga ruxsat ")

class Guest(User):
    def access_level(self):
        print(f"Mehmon kirish huquqi: {self.first_name} {self.last_name} {self.year} - faqat ko'rishga ruxsat")
    

admin = Admin("Latipova", "Sevara", 2005)
guest = Guest("Sevinch", "Latifova", 2008)

admin.access_level()
guest.access_level()