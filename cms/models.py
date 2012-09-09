from django.db import models
from django.template import Context, Template

from settings import PARENT_SEPARATOR


class Page(models.Model):
    headline = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=512, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, limit_choices_to={})
    content = models.TextField(blank=True)
    public = models.BooleanField(default=True)
    is_template = models.BooleanField(default=False)

    def get_full_slug(self):
        slug = self.slug
        if self.parent != None:
            parent = self.parent
            while parent is not None:
                slug = parent.slug + PARENT_SEPARATOR + slug
                parent = parent.parent
        return slug

    def render(self, context=None):
        if self.is_template:
            template = Template(self.content)
            if context is None:
                context = Context()
            return template.render(context)
        return self.content

    def __unicode__(self):
        return self.headline
