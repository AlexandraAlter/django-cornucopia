from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.hashers import make_password

from users.models import User


class Command(BaseCommand):
    help = 'Sets up a default superuser for development'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        if not User.objects.filter(username=settings.SUPERUSER_USERNAME).exists():
            user = settings.SUPERUSER_USERNAME
            password = make_password(settings.SUPERUSER_PASSWORD)
            admin = User(username=user, password=password, is_staff=True, is_superuser=True)
            admin.save()

            self.stdout.write(self.style.SUCCESS('Successfully set up user "%s"' % user))
        else:
            self.stdout.write(self.style.SUCCESS('Already set up user "%s"' % user))
