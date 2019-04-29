import json

from django.http import Http404
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView

from bbakdoc.events.forms import EventCreateForm
from bbakdoc.events.models import Event


# def index(request):
#     return render(request, 'events/main.html', {})
#

class EventMainView(ListView):
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views#Templates
    template_name = 'events/main.html'
    model = Event
    context_object_name = 'my_events_list'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(host=self.request.user)

    def get_context_data(self, **kwargs):
        return super(EventMainView, self).get_context_data(**kwargs)


# class BasicEventCreateView(CreateView):
#     model = BasicEvent
#     fields = ('title',)

class EventCreateView(CreateView):
    template_name = 'events/event_create.html'
    form_class = EventCreateForm

    # success_url = '/events/'

    def form_valid(self, form):
        basic_event = form.save(commit=False)
        basic_event.host = self.request.user
        basic_event.save()
        return super().form_valid(form)


class EventDetailView(DetailView):
    model = Event


def room(request, event_code):
    try:
        event = Event.get_object_by_code(event_code)
    except Event.DoesNotExist:
        raise Http404

    return render(
        request,
        'events/room.html',
        {
            'event': event
        },
    )

# def room(request, room_name):
#     return render(
#         request,
#         'events/room.html',
#         {
#           'room_name_json': mark_safe(json.dumps(room_name))
#         },
#     )
