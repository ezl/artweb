from django.db import models
from django.utils import timezone

class Message(models.Model):
    sms_message_id = models.CharField(max_length=64, unique=True)
    text_message = models.TextField()
    from_phone = models.CharField(max_length=18)
    from_country = models.CharField(max_length=2)
    from_state = models.CharField(max_length=80)
    from_city = models.CharField(max_length=80)
    from_zip = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)

class Image(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    uniqid = models.CharField(max_length=112, unique=True)
    mime_type = models.CharField(max_length=20, default="image/jpeg")
    filesize = models.IntegerField(default=0)
    content = models.TextField()


