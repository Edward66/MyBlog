import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings")
profile = os.environ.get('TYPEIDEA_PROFILE', 'product')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "typeidea.settings.%s" % profile)

application = get_wsgi_application()

