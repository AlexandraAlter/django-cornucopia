from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth.hashers import make_password


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from .models import User

        if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            password = make_password(settings.SUPERUSER_PASSWORD)
            admin = User(username=settings.SUPERUSER_USERNAME,
                         password=password,
                         is_staff=True,
                         is_superuser=True)
            admin.save()
