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
            TITLE: _('')
        }
        widgets = {
            TITLE: forms.TextInput(attrs={'placeholder': '이벤트명을 입력해주세요'})
        }
