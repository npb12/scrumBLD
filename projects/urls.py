from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from projects.views import *

urlpatterns = patterns('',
    url(r'^$', projects),
    url(r'^details/(?P<pid>\d+)/$', details),
    url(r'^edit-details/$', edit_project),
    url(r'^edit-details/(?P<pid>\d+)/$', edit_project),
    url(r'^project-skills/(?P<pid>\d+)/$', temp_project_skills),
    url(r'^add-remove-skill/(?P<pid>\d+)/(?P<sid>\d+)/(?P<ar>\w)/$', addRemoveSkill),
    url(r'^request-to-join/(?P<pid>\d+)/$', request_to_join),
    url(r'^requests/(?P<pid>\d+)/$', requests),
    url(r'^update-request/(?P<rid>\d+)/(?P<pid>\d+)/$', update_request),
)
