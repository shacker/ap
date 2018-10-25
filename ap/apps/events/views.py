from django.shortcuts import render

from ap.apps.events.models import Event


def index(request):
    '''List/search all events'''

    events = Event.objects.filter(published=True)

    return render(request, "events/index.html", {"events": events})
