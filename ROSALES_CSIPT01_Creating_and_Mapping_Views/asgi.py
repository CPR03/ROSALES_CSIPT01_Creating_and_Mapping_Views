"""
ASGI config for ROSALES_CSIPT01_Creating_and_Mapping_Views project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ROSALES_CSIPT01_Creating_and_Mapping_Views.settings')

application = get_asgi_application()
