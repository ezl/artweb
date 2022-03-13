from django.db import models
from .message import Message
from core.models import User
from django.utils import timezone
import environ

env = environ.Env()

class Image(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    views = models.IntegerField(default=0)
    uniqid = models.CharField(max_length=112, unique=True)
    mime_type = models.CharField(max_length=20, default="image/jpeg")
    filesize = models.IntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "artweb_image"

    @property
    def url(self) -> str:
        url = "http://" + env("DOMAIN_NAME") + "/pics/" + self.uniqid
        return url

    @property
    def user_username(self) -> str:
        return self.user.username

    @property
    def user_phone(self) -> str:
        return self.user.phone

    @property
    def user_email(self) -> str:
        return self.user.email

    @property
    def user_full_name(self):
        return self.user.full_name

    #property
    def user_location(self) -> str:
        return self.user.location

    @property
    def user_created_at(self) -> str:
        return self.user.created_at

    @property
    def user_profile_url(self) -> str:
        return self.user.profile_url


