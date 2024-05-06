import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_end_point = "https://api.sheety.co/36bac2d9047ecc62639b034bef885328/flightDeals/prices"
        self.sheety_header = {
            "Authorization": "bWlzaGE6QXNkZjIzMTI="
        }
        self.sheety_input = {

        }
        self.sheet_data = []
        self.sheety_request()


    def sheety_request(self):
         response = requests.get(url=self.sheety_end_point, headers=self.sheety_header, auth=("misha", "Asdf2312"))
         self.sheet_data = response.json()

    def update_iata_codes_in_sheet(self):
        for row in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.sheety_end_point}/{row['id']}",
                json=new_data,
                headers=self.sheety_header,
                auth=("misha", "Asdf2312")

            )
            # print(response.text)