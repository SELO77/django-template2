import json
import logging

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer, AsyncJsonWebsocketConsumer


# @database_sync_to_async
# def get_user_email(scope):
#     return scope.user.email
from bbakdoc.events.models import EventQuestion


class EventConsumer(AsyncJsonWebsocketConsumer):
    # class EventConsumer(WebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'event_{self.room_name}'

        # Join room group
        # Add exception handling when redis turn off
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

    @database_sync_to_async
    def create_question(self, content, questioner):
        obj = EventQuestion.objects.create(
            event_id=int(self.room_name)-1000,
            content=content,
            questioner=questioner,
        )
        return obj


    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):
        question = content['question']
        questioner = content.get('questioner', 'Anonymous')

        question_obj = await self.create_question(question, questioner)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'push_question',
                'content': question_obj.content,
                'questioner': question_obj.questioner,
                'likes': question_obj.likes,
            }
        )

    # Receive message from room group
    async def push_question(self, event):
        await self.send_json(event)
