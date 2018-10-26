import datetime
from django.shortcuts import render

from ap.apps.events.models import Event


def index(request, tense: str=None):
    '''List/search all events'''

    today = datetime.date.today()
    events = Event.objects.filter(published=True)
    if tense == "past":
        events = events.filter(start__lte=today)
        events = events.order_by('-start')
    else:
        events = events.filter(start__gte=today)
        events = events.order_by('start')

    return render(request, "events/index.html", {
        "events": events,
        "tense": tense
    })
