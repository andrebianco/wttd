"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
# from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventex.settings")

application = Cling(get_wsgi_application())

# if settings.STATIC_URL == '/static/':
#     application = Cling(get_wsgi_application())
#  else:
#      application = get_wsgi_application()
