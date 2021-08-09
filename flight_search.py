import requests
from datetime import datetime
from data_manager import DataManager
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()


TEQUILA_SEARCH_ENDPOINT = "tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
TEQUILA_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_HEADER = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data: DataManager):
        self.data = data

    def retrieve_iata(self):
        sheet_data = self.data.retrieve_sheets()
        cities = [city['city'] for city in sheet_data['prices']]

        for city in cities:
            parameters = {
                "term": f"{city}",
                "location_types": "city"
            }
            response = requests.get(url=TEQUILA_LOCATION_ENDPOINT, json=parameters, headers=TEQUILA_HEADER).json()
            iata_code = response["locations"][0]["code"]


