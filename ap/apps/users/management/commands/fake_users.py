from django.core.management.base import BaseCommand

from ap.apps.events.factories import EventFactory
from ap.apps.orgs.factories import OrgFactory
from ap.apps.users.factories import UserFactory

NUM_ORGS = 25
NUM_USERS = 100
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
