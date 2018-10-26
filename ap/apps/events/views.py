import datetime
from django.shortcuts import render

from ap.apps.events.models import Event


def index(request):
    '''List/search all eventss'''

    today = datetime.date.today()
    events_future = Event.objects.filter(published=True, start__gte=today).order_by('start')

    return render(request, "events/index.html", {"events_future": events_future})
