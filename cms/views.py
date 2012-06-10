from django.views.generic import DetailView

from models import Page


class PageDetailView(DetailView):
    model = Page
