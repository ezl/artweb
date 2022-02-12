from sms2url.models import Message, Image
from django.utils import timezone
from twilio.rest import Client as twilio
import logging, requests, base64, environ
import random, string

logger = logging.getLogger('django')
env = environ.Env()

class sms():

    def receive(request):

        # Initial checks
        if request.POST.get('SmsSid') == None:
            return None

        # Check if message ID exists
        try:
            m = Message.objects.get(sms_message_id=request.POST.get("SmsSid"))
            return None
        except Message.DoesNotExist:
            logging.info("Received new SMS message with id# %s", request.POST.get("SmsSid"))

        # Add new message
        msg = Message(
            sms_message_id=request.POST.get('SmsSid'),
            text_message=request.POST.get('Body'),
            from_phone=request.POST.get('From'),
            from_country=request.POST.get('FromCountry'),
            from_state=request.POST.get('FromState'),
            from_city=request.POST.get('FromCity'),
            from_zip=request.POST.get('FromZip'),
            created_at=timezone.now()
        );
        msg.save()

        # Add images
        sms.add_images(msg.id, request)

        return msg

    def add_images(msg_id, request):

        x=0
        while (True):

            if request.POST.get("MediaUrl" + str(x)) == None:
                logger.error("Breaking with %s", str(x))
                break

            # Get contents
            try:
                res = requests.get(request.POST.get("MediaUrl" + str(x)))
            except:
                logger.warning("Unable to retrieve image at %s", request.POST.get("MediaUrl" + str(x)))
                continue

            # Add image
            uniqid = sms.generate_uniqid()
            img = Image(
                message_id = msg_id,
                uniqid = uniqid,
                mime_type = request.POST.get("MediaContentType" + str(x)),
                content = base64.b64encode(res.content)
            )
            img.save()

            # Send message
            sms.send(request.POST.get("From"), uniqid)
            x = x + 1

    def send(phone, uniqid):

        # Set message
        url = "http://" + env("DOMAIN_NAME") + "/pics/" + uniqid
        message = "Thanks, and your image can be found at:\n\n" + url

        # Send SMS
        if env("SMS_TYPE") == "nexmo":
            sms.send_nexmo(phone, message)
        else:
            logger.error("Sending via Twilio")
            sms.send_twilio(phone, message)

    def send_twilio(phone, message):

        # Send sms message
        client = twilio(env("TWILIO_SID"), env("TWILIO_AUTH_TOKEN"))
        client.messages.create(
            from_ = env("TWILIO_SENDER"),
            to = phone,
            body = message
        )

    def send_nexmo(phone, message):

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

    def generate_uniqid():

        uniqid = ""
        while (True):

            uniqid = ''.join(random.choice(string.ascii_letters) for i in range(10))
            try:
                row = Image.objects.get(uniqid=uniqid)
            except:
                break

        return uniqid


