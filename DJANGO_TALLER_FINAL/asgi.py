import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGO_TALLER_FINAL.settings')

application = get_asgi_application()
