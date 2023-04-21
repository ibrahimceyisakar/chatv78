from django.urls import path, include
from chat.consumers import ChatConsumer
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# Here, "" is routing to the URL ChatConsumer which
# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"messages/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(
        r"$/messages/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()
    ),  # try to remote it later
]
