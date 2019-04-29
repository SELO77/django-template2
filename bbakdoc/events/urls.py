from django.urls import path

from bbakdoc.events.views import (
    room, EventCreateView, EventMainView, EventDetailView)

app_name = 'events'


urlpatterns = [
    path('', view=EventMainView.as_view(), name='main'),
    path('create/', view=EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/', view=EventDetailView.as_view(), name='event_detail'),
    path('rooms/<int:event_code>/', view=room, name='event_room'),
]
