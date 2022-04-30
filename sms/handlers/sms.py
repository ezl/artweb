from services.sms import twilio, nexmo
from sms.models.image import Image
from sms.models.message import Message
from core.models import User
from django.utils import timezone
import logging
import base64
import environ
import random
import string

logger = logging.getLogger('django')
env = environ.Env()


class sms():

    def receive(
            message_id: str,
            body: str,
            sender: User
    ) -> Message:

        # Check if message ID exists
        try:
            m = Message.objects.get(sms_message_id=message_id)
            return m
        except Message.DoesNotExist:
            logging.info("Received new SMS message with id# %s", message_id)

        # Add new message
        msg = Message(
            user_id=sender.id,
            sms_message_id=message_id,
            text_message=body,
            created_at=timezone.now()
        )
        msg.save()

        return msg

    # Add new image
    def add_image(
            msg_id: str,
            user: User,
            is_first: bool,
            mime_type: str,
            contents
    ) -> Image:

        uniqid = sms.generate_uniqid()
        img = Image(
            message_id=msg_id,
            user_id=user.id,
            uniqid=uniqid,
            mime_type=mime_type,
            content=base64.b64encode(contents)
        )
        img.save()

        # Send SMS message
        msg_alias = "MSG_FIRST_IMAGE" if is_first else "MSG_RECURRING_IMAGE"
        sms.send(user, env(msg_alias), uniqid)

        return img

    # Send SMS message
    def send(user: User, message: str, uniqid=None):

        # Replace url in message, if needed
        if uniqid is not None:
            url = "http://" + env("DOMAIN_NAME") + "/pics/" + uniqid
            message = message.replace("~url~", url)
        message = message.replace("~profile_url~", user.profile_url)
        message = message.replace("\\n", "\n")

        # Send SMS
        if env("SMS_TYPE") == "nexmo":
            nexmo.api.send(user.phone, message)
        else:
            twilio.api.send(user.phone, message)

    def generate_uniqid(self):
        """
        Generate unique id
        :return:
        """

        uniqid = ""
        while (True):

            uniqid = ''.join(random.choice(string.ascii_letters) for i in range(10))
            try:
                Image.objects.get(uniqid=uniqid)
            except Exception:
                break

        return uniqid
