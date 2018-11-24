from django import forms

from ap.apps.events.models import Event


class EventManagementForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = [
            'title',
            'event_type',
            'about',
            'start',
            'place_name',
            'city',
            'state_province',
            'country',
            'address',
            'latitude',
            'longitude',
            'zoom',
            'official_event_site_title',
            'official_event_site_url',
        ]
