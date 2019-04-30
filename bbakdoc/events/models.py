from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class EventBaseModel(models.Model):
    title = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)
    is_end = models.BooleanField(default=False)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    ts_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def code(self):
        return self.id + 1000

    @classmethod
    def get_active_event_by_code(cls, code):
        pk = code - 1000
        return cls.objects.get(pk=pk, is_active=True)


class Event(EventBaseModel):
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.code}:{self.title}'

    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.id])


class EventQuestion(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    questioner = models.CharField(max_length=20)
    likes = models.PositiveIntegerField(default=0)
    is_show = models.BooleanField(default=True)
    ts_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:30]

    @classmethod
    def get_event_questions_list(cls, event_id):
        return cls.objects.filter(event_id=event_id,
                                  is_show=True).order_by('-like')
