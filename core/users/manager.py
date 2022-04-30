from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(
            self,
            phone: str,
            country=None,
            state=None,
            city=None,
            zip=None,
            username=None,
            password=None
    ):

        if not phone:
            raise ValueError("Users must have an phone address")
        elif not username:
            username = phone

        user, created = self.get_or_create(
            username=username,
            phone=phone,
        )

        # Set location, if first user
        if created:
            user.country = country
            user.state = state
            user.city = city
            user.zip = zip
            user.save()

        # Set password, if we hav one
        if password:
            user.set_password(password)

        return [user, created]

    def create_superuser(
            self,
            username: str,
            password: str
    ):

        user, created = self.create_user(
            phone=username,
            username=username,
            password=password,
        )

        # Set as admin
        user.admin = True
        user.save()

        return user
