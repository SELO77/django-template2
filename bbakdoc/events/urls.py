from django.urls import path

from bbakdoc.events.views import (
    index,
    room)

app_name = 'events'
urlpatterns = [
    path('', view=index, name='main'),
    path('<str:room_name>/', view=room, name='room'),
]
