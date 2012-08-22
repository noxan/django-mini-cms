from django import template
from django.core.urlresolvers import reverse


register = template.Library()

class BreadcrumbsListNode(template.Node):
    def render(self, context):
        page = context['object']

        builder = []
        builder.append('<ul class="breadcrumb">')
        parent = page.parent
        while parent is not None:
            builder.append(u'<li><a href="%s">%s</a> <span class="divider">/</span></li>' % (reverse('cms:page', args=[parent.slug]), parent.headline))
            parent = parent.parent
        builder.append(u'<li class="active">%s</li>' % (page.headline))
        builder.append(u'</ul>')
        return u''.join(builder)

@register.tag
def render_breadcrumbs(parser, token):
    return BreadcrumbsListNode()


