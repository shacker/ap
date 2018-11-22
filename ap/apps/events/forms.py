from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

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
            'official_event_site_url',
            'official_event_site_title',
            'organizers',
            'organizations',
            'published',
        ]
