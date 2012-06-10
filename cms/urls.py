from django.conf.urls import patterns, include, url

from views import PageDetailView


urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9]+)/$', PageDetailView.as_view(), name='page'),
)
