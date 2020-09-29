from django.conf import settings
from django.db import models


class Zone(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT,
                              blank=True,
                              null=True)

    name = models.CharField(max_length=256)
