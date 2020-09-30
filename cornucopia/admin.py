from django.contrib import admin

from . import models


@admin.register(models.posts.Post)
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.posts.Gallery)

admin.site.register(models.reports.Report)

@admin.register(models.tags.TagCategory)
class TagCategoryAdmin(admin.ModelAdmin):
    list_filter = ('zone',)
    pass

admin.site.register(models.tags.Tag)
admin.site.register(models.tags.TagImplication)
admin.site.register(models.tags.TagAlias)

admin.site.register(models.users.User)

admin.site.register(models.zones.Zone)
