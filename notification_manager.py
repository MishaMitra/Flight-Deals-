from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = 'AC2069daa6fbde439da15485749c546d0d'
        self.auth_token = '0ae66afcfc72d2a224fffddd8c65d551'

    def sms_send(self,price,origin_city,origin_airport,destination_city,destination_airport,out_date,return_date):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_='+16562211078',
            body=f"Low price alert\n"
                 f"only ${price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport},\n"
                 f"from {out_date} to {return_date}",
            to='+37455133130'
        )
