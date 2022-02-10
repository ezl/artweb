from django.shortcuts import render
from django.http import HttpResponse
from sms2url.handlers.sms import sms
import logging

logger = logging.getLogger('django')

def receive(request):

    # Receive SMS message
    msg = sms.receive(request)
    if msg == None:
        logger.error("Unable to process incoming SMS request.")
        return HttpResponse("Invalid Request", status=400)

    return HttpResponse(msg.id)




