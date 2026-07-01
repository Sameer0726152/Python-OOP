class Notification:
    def send(self):
        print("Sending Notification")

class EmailNotification(Notification):

    def __init__(self, recipient, subject):
        self.recipient = recipient
        self.subject = subject

    def send(self):
        super().send()
        print("Sending Email\n")

class SMSNotification(Notification):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self):
        super().send()
        print("Sending SMS\n")

class PushNotification(Notification):

    def __init__(self, device_id, app_name):
        self.device_id = device_id
        self.app_name = app_name

    def send(self):
        super().send()
        print("Pushing Notification\n")

notifications = [EmailNotification("Nihar", "IDK"), SMSNotification(9595212305), PushNotification(12, "Whatsapp")]
for i in notifications:
    i.send()

def notify(notificate):
    notificate.send()

notify(EmailNotification("Nihar", "IDK"))
notify(SMSNotification(9595212305))
notify(PushNotification(35, "Youtube"))