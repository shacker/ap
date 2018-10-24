import factory
from django.utils.text import slugify

from ap.apps.orgs.models import Org
from ap.apps.users.models import User


class OrgFactory(factory.django.DjangoModelFactory):
    """Fabricate an organization with realistic data"""
    class Meta:
        model = Org

    name = factory.Faker('company')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    human = factory.LazyAttribute(lambda o: User.objects.all().order_by('?').first())
