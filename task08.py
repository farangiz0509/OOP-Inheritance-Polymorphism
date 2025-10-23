class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self):
        raise NotImplementedError("Bunday metod mavjud emas!")

    def get_interest(self):
        raise NotImplementedError("Bunday metod mavjud emas!")



class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} so'm yechildi.Qolgan balans: {self.balance}")

        else:
            print("Mablag' yetarli emas!")


    def get_interest(self):
        interest = self.balance * 0.05
        print(f"Foiz: {interest}")
        return interest

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} so'm yechildi. Qolgan hisob: {self.balance}")

    def get_interest(self):
        print("Foiz mavjud!")
        return 0
    
savings = SavingsAccount(1200000)
cheking = CheckingAccount(4000000)


savings.withdraw(2000000)
savings.get_interest()

cheking.withdraw(9000000)
cheking.get_interest()