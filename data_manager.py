import requests
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

SHEETY_GET_API_KEY = os.getenv("SHEETY_GET_API_KEY")
SHEETY_POST_API_KEY = os.getenv("SHEETY_POST_API_KEY")
HEADER = {"Authorization": f"Bearer {os.getenv('SHEETY_AUTH')}"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass

    def retrieve_sheets(self):
        """Retrieves the Google sheets via the API in JSON format"""
        response = requests.get(url=SHEETY_GET_API_KEY, headers=HEADER)
        return response.json()


    # def update_row(self):
    #     SHEETY_PUT_API = "https://api.sheety.co/5f7bebf51e96e73ce7d6cb184e070fd4/flightDeals/prices/[Object ID]"
    #
