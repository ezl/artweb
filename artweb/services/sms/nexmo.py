
import environ, logging, requests

env = environ.Env()
logger = logging.getLogger('django')

class Nexmo(object):

    # Send sms message
    def send(self, to: str, message: str):

        req = {
            'api_key': env("NEXMO_API_KEY"),
            'api_secret': env("NEXMO_API_SECRET"),
            'from': env("NEXMO_SENDER"),
            'type': 'text',
            'to': phone,
            'text': message
    }

        res = requests.post('https://rest.nexmo.com/sms/json', data=req)
        print(res.json)

api = Nexmo()

