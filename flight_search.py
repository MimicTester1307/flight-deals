import requests
from datetime import datetime,timedelta
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

CURRENT_CITY = "ACC,GH"

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data: DataManager):
        self.data = data

    def retrieve_iata(self, city: str):
        """Retrieves the IATA code for the given city"""
        parameters = {
            "term": f"{city}",
            "location_types": "city"
        }
        response = requests.get(url=TEQUILA_LOCATION_ENDPOINT, params=parameters, headers=TEQUILA_HEADER).json()
        iata_code = response["locations"][0]["code"]

        return iata_code

    def find_cheapest_flight(self, city: str, min_price: float):
        """Finds the cheapest flight to a particular City"""
        minimum_price_data = None
        current_date = datetime.now()
        time_delta = timedelta(hours=4380)
        next_six_months = (current_date + time_delta).strftime("%d/%m/%Y")
        parameters = {
            "fly_from": CURRENT_CITY,
            "fly_to": city,
            "date_from": current_date.strftime("%d/%m/%Y"),
            "date_to": next_six_months,
            "flight_type": "round"
        }
        responses = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=parameters, headers=TEQUILA_HEADER).json()
        for response in responses["data"]:
            price = response["price"]
            if price < min_price:
                minimum_price_data = response

        return minimum_price_data
