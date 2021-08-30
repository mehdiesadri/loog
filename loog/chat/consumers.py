# chat/consumers.py

import json

from channels.generic.websocket import AsyncWebsocketConsumer



class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)        

    async def connect(self):
        self.user_id = self.scope['session']['_auth_user_id']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name      

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        # room = data['room']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                # 'room': room
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            # 'room': room
        }))

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['session']['_auth_user_id']
        print("Here", self.user_id)
        self.room_name = str(self.user_id)
        self.room_group_name = 'chat_%s' % self.room_name      

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def notification_message(self, event):
        message = event.get('message')
        data = event.get('data')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'data': data
        }))
