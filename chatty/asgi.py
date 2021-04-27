import os

from django.core.asgi import get_asgi_application
import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')

application = get_asgi_application()

ws_pattern = []

application = ProtocolTypeRouter({
    "websocket" : AuthMiddlewareStack(URLRouter(
        ws_pattern
    ))
})