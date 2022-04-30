from django.http import HttpResponse, Http404
from sms.handlers.sms import sms
from sms.models.image import Image
from core.models import User
import logging
import base64
import requests
import environ

logger = logging.getLogger('django')
env = environ.Env()


def receive(request):
    # Initial checks
    if request.POST.get('SmsSid') is None:
        return None

    # Get or create user
    user, is_first = User.objects.create_user(
        request.POST.get('From').replace("+", ""),
        request.POST.get('FromCountry'),
        request.POST.get('FromState'),
        request.POST.get('FromCity'),
        request.POST.get('FromZip')
    )

    # Ensure image was received
    if request.POST.get("MediaUrl0") is None:
        sms.send(user.phone, env("MSG_NO_IMAGE_RECEIVED"))
        return HttpResponse("No image found in message received.", status=404)

    # Receive SMS message
    msg = sms.receive(
        request.POST.get('SmsSid'),
        request.POST.get('Body'),
        user
    )

    if msg is None:
        logger.error("Unable to process incoming SMS request.")
        return HttpResponse("Invalid Request", status=400)

    # Add images
    x = 0
    while (True):

        if request.POST.get("MediaUrl" + str(x)) is None:
            break

        # Get contents
        try:
            res = requests.get(request.POST.get("MediaUrl" + str(x)))
        except Exception:
            logger.warning("Unable to retrieve image at %s", request.POST.get("MediaUrl" + str(x)))
            x = x + 1
            continue

        # Add image, send SMS
        sms.add_image(
            msg.id,
            user,
            is_first,
            request.POST.get("MediaContentType" + str(x)),
            res.content
        )
        x = x + 1

    return HttpResponse(msg.id)


def display_image(request, image_id):
    try:
        img = Image.objects.get(uniqid=image_id)
    except Image.DoesNotExist:
        raise Http404("Image does not exist.")

    headers = {
        "Content-type": img.mime_type
    }
    return HttpResponse(base64.b64decode(img.content[2:]), headers=headers)
