# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

sheet_data_manager = DataManager()
flight_searcher = FlightSearch(sheet_data_manager)


# Retrieving the Google Sheets
sheet_data = sheet_data_manager.retrieve_sheets()
cities = [city['city'] for city in sheet_data['prices']]    # creating a list of cities in the list

row = 2

# updating the IATA for each city in the
for city in cities:
    iata_code = flight_searcher.retrieve_iata(city)
    sheet_data_manager.update_iata(row_number=row, data=iata_code)

    row += 1

for city in sheet_data["prices"]:
    lowest_price = city["lowestPrice"]
    minimum_price_data = flight_searcher.find_cheapest_flight(city=city['iataCode'], min_price=lowest_price)
    print(minimum_price_data)
    if minimum_price_data:
        flight_data = FlightData(minimum_price_data)
        formatted_details = flight_data.format_flight_details()
        notifier = NotificationManager()
        notifier.send_notification(formatted_details)







print(sheet_data)
print(cities)
