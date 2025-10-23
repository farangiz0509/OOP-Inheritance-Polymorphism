class User:
    def __init__(self, name):
        self.name = name

    def interact(self):
        raise NotImplementedError("Bu metod farzand klassda aniqlanishi kerak")


class Applicant(User):
    def interact(self):
        return self.apply_to_job()

    def apply_to_job(self):
        return f"{self.name} ishga ariza topshirdi."


class Employer(User):
    def interact(self):
        return self.job()

    def job(self):
        return f"{self.name} yangi ish e'lonini joylashtirdi."


user1 = Applicant("Sevara")
user2 = Employer("Azimbek")

print(user1.interact()) 
print(user2.interact()) 