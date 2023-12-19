import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO_TALLER_FINAL.settings')

application = get_wsgi_application()
