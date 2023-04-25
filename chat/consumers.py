# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    """
    The async_to_sync(...) wrapper is required because ChatConsumer
    is a synchronous WebsocketConsumer but it is calling an asynchronous
    channel layer method. (All channel layer methods are asynchronous.)
    """

    def connect(self):
        """If you do not call accept() within the connect() method then the
        connection will be rejected and closed. You might want to reject
        a connection for example because the requesting user is not authorized
        to perform the requested action. It is recommended that accept()
        be called as the last action in connect()
        (if you choose to accept the connection)
        """
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope["user"].username
        room_group_name = self.room_group_name
        print("received %s from %s at %s" % (message, user, room_group_name))
        """Send message to room group
        An event has a special 'type' key corresponding to the name of
        the method that should be invoked on consumers that receive the event.
        """
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def chat_message(self, event):
        """An event has a special 'type' key corresponding to the name of
        the method that should be invoked on consumers that receive the event.
        """
        message = event["message"]
        print("msg7812", message)
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
