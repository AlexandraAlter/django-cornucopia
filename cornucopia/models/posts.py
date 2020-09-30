from django.contrib.contenttypes import fields as ct_fields, models as ct_models
from django.contrib.postgres import fields as pg_fields
from django.conf import settings
from django.db import models

from . import tags


class Post(models.Model):
    content_id = models.IntegerField()
    content_type = models.ForeignKey(ct_models.ContentType, on_delete=models.PROTECT)
    content = ct_fields.GenericForeignKey('content_type', 'content_id')

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    tags = models.ManyToManyField(tags.Tag, through='PostTagLink', through_fields=('post', 'tag'))

    comment = models.TextField(blank=True)
    sources = pg_fields.ArrayField(base_field=models.CharField(max_length=256), blank=True)

    poster = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.PROTECT,
                               related_name='posts')
    posted_date = models.DateTimeField(auto_now=True)

    authorizer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.PROTECT,
                                   related_name='authorized_posts',
                                   blank=True,
                                   null=True)
    authorized_date = models.DateTimeField(blank=True)

    def __repr__(self):
        return "Post({!r})".format(self.id)

    def __str__(self):
        return "Post {!s}".format(self.id)


class PostTagLink(tags.TagLink):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)

    clean = tags.TagLink.make_super_tag_cleaner('post')


class PostEdit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)

    new_desc = models.TextField(blank=True)
    old_desc = models.TextField(blank=True)

    new_sources = pg_fields.ArrayField(base_field=models.CharField(max_length=256))
    deleted_sources = pg_fields.ArrayField(base_field=models.CharField(max_length=256))

    pending = models.BooleanField()

    @property
    def applied(self):
        return not self.pending

    def clean(self):
        if self.pending and old_desc != '':
            raise ValidationError(_('Post edit cannot have an old_desc and be pending.'))
        elif self.applied and new_desc != '':
            raise ValidationError(_('Post edit cannot have an new_desc and be applied.'))


class PostTagProposedLink(PostTagLink):
    edit = models.ForeignKey(PostEdit, on_delete=models.CASCADE, related_name='new_tags')


class PostTagDestroyedLink(PostTagLink):
    edit = models.ForeignKey(PostEdit, on_delete=models.CASCADE, related_name='deleted_tags')


class Gallery(models.Model):
    title = models.CharField(max_length=256)
    posts = models.ManyToManyField(Post)

    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "galleries"
