import os
import sys

from django.core.wsgi import get_wsgi_application


sys.path.append('/home/muslu/django/pythontc/pythontc/')
sys.path.append('/home/muslu/django/pythontc/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythontc.settings")

application = get_wsgi_application()
