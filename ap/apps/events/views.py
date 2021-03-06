import datetime

from django.conf import settings
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse

from ap.apps.events.forms import EventManagementForm
from ap.apps.events.models import Event

from icecream import ic

def index(request, tense: str = None, organize: bool = False):
    """List/search all events. Distinguish between past and upcoming events.
    If organize == True, filter by events current user is allowed to manage."""

    today = datetime.date.today()

    if organize:
        if request.user.is_authenticated:
            events = request.user.organizer_to_events.all().order_by("-start")
        else:
            raise PermissionDenied
    else:
        events = Event.objects.filter(published=True)
        if tense == "past":
            events = events.filter(start__lte=today).order_by("-start")
        else:
            events = events.filter(start__gte=today).order_by("start")

    paginator = Paginator(events, 10)  # num per page
    page = request.GET.get("page")
    events_list = paginator.get_page(page)

    ctx = {
        "events_list": events_list,
        "tense": tense,
        "organize": organize
    }

    return render(request, "events/index.html", ctx)


def detail(request, event_id: int, event_slug: str = None):
    """Details for a specific event"""

    event = get_object_or_404(Event, id=event_id)

    return render(request, "events/detail.html", {"event": event, "google_api_key": settings.GOOGLE_API_KEY})


def organize_event(request, event_id: int, event_slug: str = None):
    """Event organizer controls settings for an event"""

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventManagementForm(request.POST, instance=event)
        if form.is_valid():
            ic(form.cleaned_data['start'])
            ic(form.errors)
            form.save()
            # import pdb; pdb.set_trace()
            messages.success(request, f"Event saved successfully: {event.title}")
            return redirect(reverse('events:organizers_index'))
        else:
            ic(form.cleaned_data['start'])
            ic(form.data['start'])  # problem field

    else:
        form = EventManagementForm(instance=event)

    ctx = {
        "event": event,
        "form": form,
        "google_api_key": settings.GOOGLE_API_KEY
    }
    return render(request, "events/organize_event.html", ctx)


def search(request):
    """Display results of search for Event records.
    """

    q = request.GET.get("q") if request.GET.get("q") else None

    if q:
        qs = Event.objects.filter(
            Q(title__icontains=q) |
            Q(about__icontains=q) |
            Q(place_name__icontains=q) |
            Q(city__icontains=q)
        ).order_by("-start")
    else:
        # q = None
        qs = Event.objects.none()

    paginator = Paginator(qs, 10)
    page = request.GET.get("page")
    items = paginator.get_page(page)

    context = {"items": items, "q": request.GET.get("q")}
    return render(request, "events/search.html", context)
