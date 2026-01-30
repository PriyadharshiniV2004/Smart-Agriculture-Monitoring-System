from twilio.rest import Client
from utils.config import TWILIO_SID, TWILIO_AUTH, TWILIO_FROM, TWILIO_TO

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_sms(message):
    msg = client.messages.create(
        body=message,
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )
    print("📩 SMS sent:", message)
