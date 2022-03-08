from django.db import models
from django.utils import timezone
from artweb.core.models import User

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sms_message_id = models.CharField(max_length=64, unique=True)
    text_message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "artweb_message"


