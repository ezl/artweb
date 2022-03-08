from twilio.rest import Client as twilio
from functools import cached_property
import environ, logging

env = environ.Env()
logger = logging.getLogger('django')

class Twilio(object):

    @cached_property
    def client(self):
        return twilio(env("TWILIO_SID"), env("TWILIO_AUTH_TOKEN"))

    # Send sms message
    def send(self, to: str, message: str):
        print("Sending to " + to + "\n\n")
        res = self.client.messages.create(
            from_ = env("TWILIO_SENDER"),
            to = to,
            body = message
        )
        print(res)

api = Twilio()

