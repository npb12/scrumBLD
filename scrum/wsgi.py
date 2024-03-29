"""
WSGI config for scrum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/var/www')
sys.path.append('/var/www/scrumbld')
os.environ['DJANGO_SETTINGS_MODULE'] = "scrum.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
