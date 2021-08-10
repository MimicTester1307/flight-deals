import requests
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

SHEETY_GET_API_KEY = os.getenv("SHEETY_GET_API_KEY")
SHEETY_POST_API_KEY = os.getenv("SHEETY_POST_API_KEY")
SHEETY_PUT_API = os.getenv("SHEETY_PUT_API")
HEADER = {"Authorization": f"Bearer {os.getenv('SHEETY_AUTH')}"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass

    def retrieve_sheets(self):
        """Retrieves the Google sheets via the API in JSON format"""
        response = requests.get(url=SHEETY_GET_API_KEY, headers=HEADER)
        return response.json()

    def update_iata(self, row_number: int, data: str):
        """Updates the IATA code in each row
        :param row_number object_id representing which row is to be updated
        :param data the data to update the row with"""
        parameters = {
            "price": {
                "iataCode": data,
            }
        }
        requests.put(url=f"{SHEETY_PUT_API}/{row_number}", json=parameters, headers=HEADER)

