from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import DetailView

from models import Page


ERROR404_MESSAGE = ("No %(verbose_name)s found matching the query") % {'verbose_name': Page._meta.verbose_name}

class PageDetailView(DetailView):
    model = Page

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg, None)
        slug_field = self.get_slug_field()

        slug_parts = slug.split('/')

        try:
            obj = queryset.get(**{slug_field: slug_parts[-1]})
        except ObjectDoesNotExist:
            raise Http404(ERROR404_MESSAGE)

        if len(slug_parts) == 1:
            if obj.parent is not None:
                raise Http404(ERROR404_MESSAGE)
        else:
            for i in reversed(range(len(slug_parts)-1)):
                if not (obj.parent.slug == slug_parts[i]):
                    raise Http404(ERROR404_MESSAGE)

        return obj
