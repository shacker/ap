import random
from typing import Any

import factory
import pytz
from django.utils.text import slugify

from ap.apps.events.models import EVENT_TYPE_CHOICES, Event, Organization
from ap.apps.users.constants import COUNTRY_CHOICES
from ap.apps.users.models import User
from ap.apps.events.factory_data import RANDOM_EVENT_LIST, RANDOM_COORDS_LIST


class EventFactory(factory.django.DjangoModelFactory):
    """Fabricate an event with realistic data"""
    class Meta:
        model = Event

    name = factory.LazyAttribute(lambda o: random.choice(RANDOM_EVENT_LIST))
    event_type = factory.LazyAttribute(lambda o: random.choice(EVENT_TYPE_CHOICES)[0])
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    start = factory.Faker('date_time_this_century', tzinfo=pytz.UTC)
    city = factory.Faker('city')
    state_province = factory.Faker('state')
    country = factory.LazyAttribute(lambda o: random.choice(COUNTRY_CHOICES)[0])
    address = factory.Faker('street_address')
    official_event_site_url = factory.Faker('url')
    official_event_site_title = factory.Faker('text', max_nb_chars=100)
    human = User.objects.all().order_by('?').first()
    fee = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    fee_paid = factory.Faker('pybool')
    notes = factory.Faker('paragraph')
    published = True

    @factory.post_generation
    def maybe_add_orgs(obj, build: bool, extracted: Any, **kwargs: dict) -> None:
        # Maybe assign a random org to generated event.
        dice = random.choice(range(1, 5))
        for _ in range(dice):
            org = Organization.objects.all().order_by('?').first()
            obj.organizations.add(org)

    @factory.post_generation
    def add_coords(obj, build: bool, extracted: Any, **kwargs: dict) -> None:
        # Select from actual city coordinates guaranteed to be on land
        coords = random.choice(RANDOM_COORDS_LIST)
        obj.latitude = coords[0]
        obj.longitude = coords[1]


class OrgFactory(factory.django.DjangoModelFactory):
    """Fabricate an organization with realistic data"""
    class Meta:
        model = Organization

    name = factory.Faker('company')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    human = factory.LazyAttribute(lambda o: User.objects.all().order_by('?').first())
