from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from core.users.manager import UserManager
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

    is_superuser = models.BooleanField(default=False)  # TODO delete

    @property
    def profile_url(self) -> str:
        url = "http://" + env("DOMAIN_NAME") + "/user/" + self.username
        return url

    @property
    def location(self) -> str:

        if self.country is None:
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

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    @property
    def is_staff(self):
        # All superusers are staff
        return self.is_admin
