import os
from twilio.rest import Client
import smtplib


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

    def send_email(self, to_send, msg):
        user = os.environ.get('EMAIL_ID')
        password = os.environ.get('EMAIL_PASS')
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.send_message(from_addr=user, to_addrs=to_send, msg=msg)
            connection.close()
