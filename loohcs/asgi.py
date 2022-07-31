"""
ASGI config for loohcs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""


import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loohcs.settings')
django.setup()
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import earthling.routing




application = ProtocolTypeRouter( {
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack( URLRouter( earthling.routing.websocket_urlpatterns ) ),
} )