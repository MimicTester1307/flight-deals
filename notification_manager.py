import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

# loading environment variables
load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')
MY_EMAIL = os.getenv('TEST_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.__client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_notification(self, message: str):
        """Notifies the given number about the flight details
        :param message the message to be sent to the given number"""
        response = self.__client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        return response.status

    def send_email(self, message: str, email: str):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=message.encode("utf-8")
            )
