from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from projects.views import *

urlpatterns = patterns('',
    url(r'^$', projects),
    url(r'^details/(?P<pid>\d+)/$', details),
    url(r'^project-details/$', edit_project),
    url(r'^project-details/(?P<pid>\d+)/$', edit_project),
)
