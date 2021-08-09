import requests

SHEETY_GET_API_KEY = "https://api.sheety.co/5f7bebf51e96e73ce7d6cb184e070fd4/flightDeals/prices"
SHEETY_POST_API_KEY = "https://api.sheety.co/5f7bebf51e96e73ce7d6cb184e070fd4/flightDeals/prices"
HEADER = {"Authorization": "Bearer AF79wN!NAHb4&YR"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        pass

    def retrieve_sheets(self):
        response = requests.get(url=SHEETY_GET_API_KEY, headers=HEADER)
        return response.json()


    # def update_row(self):
    #     SHEETY_PUT_API = "https://api.sheety.co/5f7bebf51e96e73ce7d6cb184e070fd4/flightDeals/prices/[Object ID]"
    #
