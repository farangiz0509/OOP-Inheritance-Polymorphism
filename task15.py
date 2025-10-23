class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        raise NotImplementedError("Bunday metod hali mavjud eams!")

    def defend(self):
        raise NotImplementedError("Bunday metod hali mavjud eams!")

class Warrior(Character):

    def attack(self):
        return f"{self.name} pichoq bilan hujum qildi!"
    
    def defend(self):
        return f"{self.name} qalchon bilan himoyalandi."
    

class Mage(Character):

    def attack(self):
        return f"{self.name} sehr bilan hujum qildi!"
    
    def defend(self):
        return f"{self.name} sehrli to'siq bilan himoyalandi."
    

class Archer(Character):
    def attack(self):
        return f"{self.name} kamondan o'q uzdi!"
    
    def defend(self):
        return f"{self.name} qochib qoldi."
    

hujumchilar = [
    Warrior("Azimbek"),
    Mage("Sevara"),
    Archer("Ali")
]

for hujumchi in hujumchilar:
    print(hujumchi.attack())
    print(hujumchi.defend())
    print()