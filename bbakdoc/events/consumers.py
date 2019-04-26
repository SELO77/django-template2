import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


# @database_sync_to_async
# def get_user_email(scope):
#     return scope.user.email


class EventConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'event_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        email = self.scope['user'].email

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'email': email,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        email = event.get('email', self.channel_name)
        # user = event['user']

        await self.send(
            text_data=json.dumps({
                'message': message,
                # 'user': user,
                'email': email,
            })
        )
