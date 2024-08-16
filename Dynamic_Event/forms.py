from django import forms
from .models import Event, Session

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location']

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'start_time', 'end_time', 'event']
