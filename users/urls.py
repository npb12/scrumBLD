from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from users.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^profile/$', profile),
    url(r'^messages/$', messages),
    url(r'^friends/$', friends),
    url(r'^projects/$', projects),
    url(r'^requests/$', requests),
    url(r'^logged-out/$', TemplateView.as_view(template_name = "registration/logout.html")),
)
