from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from .manager import UserManager
import environ

env = environ.Env()

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, null=True, blank=True, default=None, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True, default=None)
    phone = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=True, default=None, verbose_name="E-Mail Address")
    full_name = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Full Name")
    country = models.CharField(max_length=2, null=True, blank=True, default=None)
    state = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="Province / State")
    city = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="City")
    zip = models.CharField(max_length=20, null=True, blank=True, default=None, verbose_name="PPostal / Zip Code")
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'username'
    objects = UserManager()

    @property
    def profile_url(self) ->str:
        url = "http://" + env("DOMAIN_NAME") + "/user/" + self.username
        return url

    @property
    def location(self) -> str:

        if self.country == None:
            return self.phone
        else:
            location = self.city + ", " + self.state + ", " + self.country
            return location

    def get_full_name(self):
        return self.__str__()

    def get_short_name(self):
        return self.phone

    @property
    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = "artweb_user"


