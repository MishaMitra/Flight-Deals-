
import requests
from flight_data import FlightData
from datetime import datetime,timedelta
import pprint

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_end_points = "https://api.tequila.kiwi.com/locations/query"
        self.headers = {"apikey": "IMydAZKHlgOkYXW34-BSZ4myl3lJJnzm"}


    def give_a_iata(self, city_name):

        params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=self.tequila_end_points, headers=self.headers, params=params)
        iata_data = response.json()["locations"]
        return iata_data[0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": "IMydAZKHlgOkYXW34-BSZ4myl3lJJnzm"}
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 5,
            "curr": "USD"
        }
        # print(params)
        response = requests.get(url="https://api.tequila.kiwi.com/v2/search",
                                headers=headers, params=params)
        try:
            data = response.json()["data"][0]
            # pprint.pp(data[0])
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["local_departure"].split("T")[0],
            return_date=data["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

