from django.shortcuts import render
from django.http import HttpResponse, Http404
from sms2url.handlers.sms import sms
from .models import Image
import logging, base64

logger = logging.getLogger('django')

def receive(request):

    # Receive SMS message
    msg = sms.receive(request)
    if msg == None:
        logger.error("Unable to process incoming SMS request.")
        return HttpResponse("Invalid Request", status=400)

    return HttpResponse(msg.id)

def display_image(request, image_id):

    try:
        img = Image.objects.get(uniqid=image_id)
    except Image.DoesNotExist:
        raise Http404("Image does nto exist.")

    headers = {
        "Content-type": img.mime_type
    }
    return HttpResponse(base64.b64decode(img.content), headers=headers)



