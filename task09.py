class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")

class EmailNotification(Notification):
    def send(self):
        print(f"Emailingizga xabar yuborildi.{self.message}: Foydalanuvchi xabarni qabul qildi {self.recipient}")

class SMSNotification(Notification):
    def send(self):
        print(f"Sms yuborildi.{self.message}: Foydalanuvchi smsni qabul qildi {self.recipient}.")

emailNotification = EmailNotification("sevapova23@gmail.com", "Bugun juda issiq bo'ldi")
smsNotification = SMSNotification("+998903452307", "Ertaga uyimga kelasanmi!?")


emailNotification.send()
smsNotification.send()