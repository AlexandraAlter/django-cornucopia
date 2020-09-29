from django.db import models
from django.conf import settings as s

from . import posts


class Report(models.Model):
    post = models.ForeignKey(posts.Post,
                             on_delete=models.PROTECT,
                             related_name='reports',
                             blank=True,
                             null=True)
    user = models.ForeignKey(s.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateTimeField()
    reason = models.CharField(max_length=256)
    message = models.TextField()
