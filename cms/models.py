from django.db import models


class Page(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    content = models.TextField(blank=True)
    public = models.BooleanField(default=True)
