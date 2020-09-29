from django.db import models


class TagCategory(models.Model):
    name = models.CharField(max_length=64)


class Tag(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(TagCategory, on_delete=models.PROTECT)


class TagLink(models.Model):
    class Meta:
        abstract = True

    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    super_tag = models.ForeignKey('self',
                                  on_delete=models.PROTECT,
                                  blank=True,
                                  null=True,
                                  related_name='+')

    def make_super_tag_cleaner(field, determinant='id'):
        def clean(self):
            # Ensure super tags refer to models with the same id
            s_id = getattr(getattr(self.super_tag, field), determinant)
            id = getattr(getattr(self, field), determinant)
            if s_id == id:
                raise ValidationError(_('Tags and super-tags must refer to the same model.'))

        return clean


class TagImplication(models.Model):
    original_tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='+')
    new_tag = models.ForeignKey(Tag, on_delete=models.PROTECT, related_name='+')


class TagAlias(models.Model):
    name = models.CharField(max_length=64)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
