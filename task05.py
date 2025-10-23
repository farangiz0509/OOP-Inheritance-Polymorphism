class Appliance():
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        raise NotImplementedError("Hali bunday metod yo'q")

    def turn_off(self):
        raise NotImplementedError("Hali bunday metod yo'q")


class TV(Appliance):
    def turn_on(self):
        print(f"Televizor:{self.name} yoqildi.")

    def turn_off(self):
        print(f"Televizor: {self.name} o'chirildi.")


class Fridge(Appliance):
    def turn_on(self):
        print(f"Muzlatkich:{self.name} yoqildi.")

    def turn_off(self):
        print(f"Muzlatkich: {self.name} o'chirildi.")


tv = TV("Artel")
fridge = Fridge("Samsung")

tv.turn_on()
tv.turn_off()


fridge.turn_on()
fridge.turn_off()