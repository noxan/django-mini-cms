from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.utils.translation import ugettext as _
from django.views.generic import DetailView

from models import Page
from settings import PARENT_SEPARATOR


ERROR404_MESSAGE = ("No %(verbose_name)s found matching the query") % {'verbose_name': Page._meta.verbose_name}

class PageDetailView(DetailView):
    model = Page

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug_full = self.kwargs.get(self.slug_url_kwarg, None)
        slug_field = self.get_slug_field()

        slug = slug_full.split(PARENT_SEPARATOR)[-1]

        try:
            obj = queryset.get(**{slug_field: slug})
        except ObjectDoesNotExist:
            raise Http404(ERROR404_MESSAGE)

        if not obj.get_full_slug() == slug_full:
            raise Http404(ERROR404_MESSAGE)

        return obj
