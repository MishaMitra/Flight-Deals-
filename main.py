#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime,timedelta
from notification_manager import NotificationManager
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
notification_manager = NotificationManager()
print(data_manager.sheet_data)

sheet_data = data_manager.sheet_data["prices"]
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]['iataCode'] == "":
    for row in sheet_data:
        # print(row)
        row['iataCode'] = flight_search.give_a_iata(row["city"])
    print(f"sheet_data:\n {sheet_data}")

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(ORIGIN_CITY_IATA, destination_city_code=destination["iataCode"],
                                         from_time=tomorrow,to_time=six_month_from_today)
    if flight.price < destination["lowestPrice"]:
        print("GOT IT")
        notification_manager.sms_send(flight.origin_city, flight.origin_airport,
                                      flight.destination_city,
                                      flight.destination_airport, flight.out_date,
                                      flight.return_date)

data_manager.sheet_data = sheet_data
data_manager.update_iata_codes_in_sheet()