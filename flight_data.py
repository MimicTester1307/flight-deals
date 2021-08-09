class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_details: dict):
        self.flight_details = flight_details

    def format_flight_details(self):
        price = self.flight_details["price"]
        from_location = f"{self.flight_details['cityFrom']}-{self.flight_details['flyFrom']}"
        to_location = f"{self.flight_details['cityTo']}-{self.flight_details['flyTo']}"

        formatted_message = f"Low price alert! Only ${price} ro fly from {from_location} to {to_location}"
