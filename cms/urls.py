from django.conf.urls import patterns, include, url

from settings import PARENT_SEPARATOR
from views import PageDetailView


urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9' + PARENT_SEPARATOR + ']+)/$', PageDetailView.as_view(), name='page'),
)
