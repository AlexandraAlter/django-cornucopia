from django.contrib.postgres import fields as pg_fields
from django.conf import settings
from django.db import models


class User(models.Model):
    base = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __repr__(self):
        return "User({!r})".format(self.base.username)

    def __str__(self):
        return "User {!s}".format(self.base.username)

