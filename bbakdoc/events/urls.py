from django.urls import path

from bbakdoc.events.views import (
    EventCreateView, EventMainView, EventDetailView, EventRoomView, EventToggleActivateView)

app_name = 'events'


urlpatterns = [
    path('', view=EventMainView.as_view(), name='page'),
    path('create/', view=EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/', view=EventDetailView.as_view(), name='event_detail'),
    path('<int:pk>/activate/', view=EventToggleActivateView.as_view(), name='event_detail'),
    path('rooms/<int:event_code>/', view=EventRoomView.as_view(), name='event_room'),
]
