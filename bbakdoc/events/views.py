import names
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, TemplateView, View

from bbakdoc.events.forms import EventCreateForm
from bbakdoc.events.models import Event, EventQuestion


# LoginRequiredMixin
# https://devlog.jwgo.kr/2016/11/26/django-login-validation-check/
class EventMainView(LoginRequiredMixin, ListView):
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

class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'events/event_create.html'
    form_class = EventCreateForm

    # success_url = '/events/'

    def form_valid(self, form):
        basic_event = form.save(commit=False)
        basic_event.host = self.request.user
        basic_event.save()
        return super().form_valid(form)


class EventToggleActivateView(View):
    def get(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            event.is_active = not event.is_active
            event.save()
            return HttpResponseRedirect(reverse('events:main'))
        except Event.DoesNotExist:
            raise Http404


class EventDetailView(DetailView):
    model = Event


class EventRoomView(TemplateView):
    template_name = 'events/room.html'

    def get_context_data(self, **kwargs):
        if not self.request.session.get('nickname'):
            self.request.session['nickname'] = names.get_last_name()

        try:
            event_code = kwargs['event_code']

            # nickname = self.request.session[f'{event_code}:n']

            event = Event.get_active_event_by_code(event_code)

            event_questions = EventQuestion.objects.filter(event_id=event.pk,
                               is_show=True).order_by('-likes')[:100]
            return {
                'event': event,
                'event_questions_list': event_questions,
            }
        except (Event.DoesNotExist, KeyError):
            raise Http404

#
# def room(request, event_code):
#     try:
#         event = Event.get_object_by_code(event_code)
#     except Event.DoesNotExist:
#         raise Http404
#
#     return render(
#         request,
#         'events/room.html',
#         {
#             'event': event
#         },
#     )

# def room(request, room_name):
#     return render(
#         request,
#         'events/room.html',
#         {
#           'room_name_json': mark_safe(json.dumps(room_name))
#         },
#     )
