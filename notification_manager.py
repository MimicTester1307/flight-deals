import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# loading environment variables
load_dotenv()
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
MY_NUMBER = os.getenv('MY_NUMBER')

class NotificationManager(Client):
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_notification(self, message: str):
        """Notifies the given number about the flight details"""
        self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )

