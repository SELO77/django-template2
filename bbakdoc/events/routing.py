# WS router
from django.conf.urls import url

from bbakdoc.events.consumers import EventConsumer


websocket_urlpatterns = [
    url(r'^ws/events/(?P<room_name>[^/]+)/$', EventConsumer),
]
