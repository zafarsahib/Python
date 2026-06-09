# implement a basic notification system

# 1. I want an interface / abstract class of Notification
# abstractmethod --> send(self, message)

from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# 2. two concrete implementations of this class

# EmailNotification class
class EmailNotification(Notification):

    def __init__(self, email):
        self.email = email

    # MUST implement send()
    def send(self, message):
        print(f"Sending EMAIL to {self.email}")
        print(f"Message: {message}")


# SMSNotification class
class SMSNotification(Notification):

    def __init__(self, phone_number):
        self.phone_number = phone_number

    # MUST implement send()
    def send(self, message):
        print(f"Sending SMS to {self.phone_number}")
        print(f"Message: {message}")


# 3. then use them here

email_user = EmailNotification("zafar@gmail.com")
sms_user = SMSNotification("+1-514-123-4567")

# calling methods directly
email_user.send("Welcome to our platform!")
print("===================")

sms_user.send("Your OTP code is 1234")
print("===================")


# function that works with ANY Notification type
def notify_user(notification, message):
    notification.send(message)


print("Using notify_user function")
print("===================")

notify_user(email_user, "Your email has been verified!")
print("===================")

notify_user(sms_user, "Your parcel has arrived!")