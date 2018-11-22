import random
from typing import Any

import factory
from django.contrib.auth.models import Group
from django.db import IntegrityError

from ap.apps.users.constants import COUNTRY_CHOICES
from ap.apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Fabricate a User with realistic data"""
    class Meta:
        model = User
        django_get_or_create = ('username', )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(lambda o: f"{o.first_name.lower()}_{o.last_name.lower()}")
    email = factory.Faker('email')
    city = factory.Faker('city')
    state_province = factory.Faker('state')
    country = factory.LazyAttribute(lambda o: random.choice([x[0] for x in COUNTRY_CHOICES]))
    about = factory.Faker('text', max_nb_chars=600)
    facebook = factory.LazyAttribute(lambda o: o.username)
    instagram = factory.LazyAttribute(lambda o: o.username)
    linkedin = factory.LazyAttribute(lambda o: o.username)
    twitter = factory.LazyAttribute(lambda o: o.username)
    personal_website = factory.Faker('url')
    professional_website = factory.Faker('url')


    @factory.post_generation
    def maybe_add_groups(obj, build: bool, extracted: Any, **kwargs: dict) -> None:
        # Maybe assign a random role to generated user.
        dice = random.choice(range(5))
        if dice == 3:  # 1 in 5 chance we make this user a photographer or organizer
            group = Group.objects.all().order_by('?').first()
            obj.groups.add(group)


    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        # Override the default ``_create`` with our custom call.
        # The default would use ``manager.create(*args, **kwargs)``
        manager = cls._get_manager(model_class)
        try:
            return manager.create_user(*args, **kwargs)
        except IntegrityError:  # Username probably already exists
            pass

