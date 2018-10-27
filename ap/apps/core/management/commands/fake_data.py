import datetime
import math
from random import randint

from django.core.management.base import BaseCommand

from ap.apps.events.factories import EventFactory, OrgFactory
from ap.apps.events.models import Event
from ap.apps.users.factories import UserFactory

NUM_ORGS = 25
NUM_USERS = 500
NUM_EVENTS = 50


class Command(BaseCommand):
    help = """Generate fake model instances for QA/testing purposes"""

    def handle(self, *args, **options) -> None:

        OrgFactory.create_batch(NUM_ORGS)
        print(f"{NUM_ORGS} organizations created")

        UserFactory.create_batch(NUM_USERS)
        print(f"{NUM_USERS} users created")

        EventFactory.create_batch(NUM_EVENTS)
        print(f"{NUM_EVENTS} events created")

        # All events were created in the past. Make some of them in the future
        events = Event.objects.all()
        num = math.floor(events.count() / 4)
        future_events = events[:num]
        today = datetime.date.today()
        days_forward = randint(1, 180)
        for event in future_events:
            # Set to current year, then add x days
            start = datetime.datetime(today.year, event.start.month, event.start.day)
            event.start = start + datetime.timedelta(days=days_forward)
            event.save()
        print(f"{num} events set to occur in the future")
