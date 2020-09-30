from django.conf import settings
from django.db import models


class Zone(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.PROTECT,
                              blank=True,
                              null=True)

    name = models.CharField(max_length=256)

    def __repr__(self):
        return "Zone({!r}, {!r})".format(self.name, self.owner or None)

    def __str__(self):
        if self.owner:
            return "Zone {!s}.{!s}".format(self.owner.username, self.name)
        else:
            return "Zone {!s}".format(self.name)
