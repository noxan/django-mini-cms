from django.db import models


class Page(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={})
    content = models.TextField(blank=True)
    public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.headline
