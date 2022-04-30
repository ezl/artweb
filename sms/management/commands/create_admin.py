from django.core.management.base import BaseCommand
from core.models import User


class Command(BaseCommand):
    help = 'Create administrator in custom user model.'

    def handle(self, *args, **kwargs):
        user = User.objects.create_superuser("admin", "pass12345")
        self.stdout.write("User created: " + user.username + "\n")
