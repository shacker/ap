import random

from django.core.management.base import BaseCommand
from faker import Faker
import factory.fuzzy
import factory
from ap.apps.orgs.models import Org
from ap.apps.users.constants import COUNTRY_CHOICES
from ap.apps.users.models import User

NUM_ORGS = 25
NUM_USERS = 1000


class Command(BaseCommand):
    help = """Generate 1,000 fake users for testing purposes"""

    def handle(self, *args, **options) -> None:

        fake = Faker()
        shackadmin = User.objects.get(username='shackadmin')

        # Orgs first
        for _ in range (NUM_ORGS):
            Org.objects.create(
                name=fake.company(),
                slug=fake.word(),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.email(),
                human=shackadmin
            )

        for _ in range(NUM_USERS):
            print("----")
            p = fake.profile()
            print(p)

            try:
                personal_website = p["website"][0]
            except:
                personal_website = ''
            try:
                professional_website = p["website"][1]
            except:
                professional_website = ''

            country_ids = [x[0] for x in COUNTRY_CHOICES]

            try:
                User.objects.create_user(
                    username=p.get("username"),
                    email=p.get("mail"),
                    first_name=p.get("name").split()[0],
                    last_name=p.get("name").split()[1],
                    city=fake.city(),
                    state_provenance=fake.state(),
                    country=factory.fuzzy.FuzzyChoice(country_ids).fuzz(),
                    about=fake.text(max_nb_chars=400),
                    facebook=p.get("username"),
                    instagram=p.get("username"),
                    linkedin=p.get("username"),
                    twitter=p.get("username"),
                    personal_website=personal_website,
                    professional_website=professional_website,
                )
            except:
                # Most likely the username is already taken
                pass
