class Courier:
    def __init__(self, name):
        self.name = name

    def delivery_range(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")

    def calculate_fee(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")


class BikeCourier(Courier):
    def delivery_range(self):
        return "0-10 km oralig'ida yetkazib beradi." 
    
    def calculate_fee(self, distance):
        price = 3000
        return distance * price

class CarCourier(Courier):
    def delivery_range(self):
        return "0-30 km oralig'ida yetkazib beradi."
    
    def calculate_fee(self, distance):
        price = 6000
        return distance * price

class DroneCourier(Courier):
    def delivery_range(self):
        return "0-15 km oralig'ida havodan yetkazib beradi."
    
    def calculate_fee(self, distance):
        price = 12000
        return distance * price
    

bike = BikeCourier("Velesiped")
car = CarCourier("Kiya K5")
drone = DroneCourier("SkyBot X-15")

print(bike.name)
print(bike.delivery_range())
print("Yetkazib berish narxi:",bike.calculate_fee(10))
print()

print(car.name)
print(car.delivery_range())
print("Yetkazib berish narxi:",car.calculate_fee(25))
print()

print(drone.name)
print(drone.delivery_range())
print("Yetkazib berish narxi:",drone.calculate_fee(30))