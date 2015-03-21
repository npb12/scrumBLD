from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from projects.views import *

urlpatterns = patterns('',
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create/$', create),
)
