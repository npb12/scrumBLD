from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
admin.autodiscover()

from users.views import register


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', register),
    url(r'^landing/$', TemplateView.as_view(template_name = "pages/scrum/landing.html")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
