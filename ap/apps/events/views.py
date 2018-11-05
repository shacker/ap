import datetime

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

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

    paginator = Paginator(events, 10)  # num per page
    page = request.GET.get('page')
    events_list = paginator.get_page(page)

    return render(request, "events/index.html", {
        "events_list": events_list,
        "tense": tense
    })


def detail(request, event_id: int, event_slug: str=None):
    '''Details for a specific event'''

    event = get_object_or_404(Event, id=event_id)

    return render(request, "events/detail.html", {
        "event": event,
        "google_api_key": settings.GOOGLE_API_KEY
    })
