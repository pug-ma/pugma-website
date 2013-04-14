from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
)