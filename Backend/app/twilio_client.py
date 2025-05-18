from twilio.rest import Client
from app.settings import settings

class TwilioClient:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.from_ = settings.TWILIO_WHATSAPP_FROM

    def send(self, to, body):
        self.client.messages.create(
            from_=self.from_,
            to=f"whatsapp:{to}",
            body=body,
            status_callback=settings.STATUS_CALLBACK_URL
        )

    def send_order_confirmation(self, order):
        body = f"Hi {order.customer_name}, your order #{order.id} is confirmed."
        self.send(order.whatsapp_number, body)

    def send_status_update(self, order):
        body = f"Order #{order.id} is now {order.status}."
        self.send(order.whatsapp_number, body)

    def send_cancellation(self, order):
        body = f"Your order #{order.id} has been canceled."
        self.send(order.whatsapp_number, body)

twilio_client = TwilioClient()