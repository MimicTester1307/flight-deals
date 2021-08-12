This is a simple code interface for finding cheap flights. The code searches through a Google Sheet containing cities of interests, their International Air Transport Association (IATA) codes, and specified prices. 
It then uses the IATA codes to search for cheap flights and notifies you via SMS if any is found. It makes use of four main APIs:

- The Sheety API that turns the Google Sheet into a REST API.
- The Tequila locations API provided by Kiwi.com for retrieving the IATA codes for the cities you want to travel to.
- The Tequila search API, also provided by Kiwi.com for searching for and retrieving flight details lower than your specified price.
- The Twilio API for SMS notifications if cheaper deals are found.
