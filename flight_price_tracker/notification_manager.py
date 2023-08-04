import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.acc_sid = os.environ.get('TWILIO_ACC_SID')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.client = Client(self.acc_sid, self.auth_token)

    def send_message(self, msg):
        message = self.client.messages.create(
            from_='+16672880397',
            to='+918098230245',
            body=msg
        )
