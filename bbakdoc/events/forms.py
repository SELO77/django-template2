from django import forms
from django.utils.translation import ugettext_lazy as _

from bbakdoc.events.models import Event


TITLE = 'title'


class EventCreateForm(forms.ModelForm):
    def clean_title(self):
        return self.cleaned_data[TITLE]

    class Meta:
        model = Event
        fields = (TITLE, )
        labels = {
            TITLE: _('타이틀')
        }
        help_texts = {
            TITLE: _('이벤트 타이틀을 입력해주세요.')
        }
