from django.db import models

from settings import PARENT_SEPARATOR


class Page(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={})
    content = models.TextField(blank=True)
    public = models.BooleanField(default=True)

    def get_full_slug(self):
        slug = self.slug
        if self.parent != None:
            parent = self.parent
            while parent is not None:
                slug = slug + PARENT_SEPARATOR + parent.slug
                parent = parent.parent
        return slug

    def __unicode__(self):
        return self.headline
