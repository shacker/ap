import random
import pytz
import factory
from django.utils.text import slugify

from ap.apps.events.models import Event, EVENT_TYPE_CHOICES
from ap.apps.orgs.models import Org
from ap.apps.users.models import User

event_list = [
    'Napa Wine Country Marathon',
    'ZombieRunner Halloween',
    'Lake Chabot',
    'Santa Clarita Marathon',
    'Two Cities Marathon',
    'CATHalf and Pounding Creek Marathon',
    'Chessie Trail Fall Half Marathon',
    'Day of the Dead Marathon Series',
    'Goblin Valley Ultra',
    'Grants Pass Marathon',
    'I Ran Flagship Marathons - Estonia',
    'I Ran Marathons - Count Dracula',
    'Kansas Rails-to-Trails Fall Ultra Extravaganza',
    'Marathon on the Mountain',
    'Silver Comet Races',
    'Skydive Ultra Texas',
    'Spinx Run Fest',
    'Best of the Bay Double Century',
    'Grizzly Century',
    'The Jensie Gran Fondo of Marin',
    'Konocti Challenge',
    'Westlake Village Century',
    'Wine and Roses Bike Ride',
    'Bass Lake Powerhouse Double Century',
    'Phils Cookie Fondo',
    'Patriot Ride for our Heroes',
    'Solvang Autumn Double Century',
    'Spooktacular Century',
    'The Wildcat Gran Fondo',
    'Giro di San Diego',
    'Victor Valley Bicycle Tour',
    'Bike the Coast',
    'Swamdo / Swami\'s Fondo',
    'Palm Desert Century',
    'Tour de Foothills',
    '2018 Postal Two-Mile Relay (USMS)',
    'University of Miami Orange and Green Meet (College Club)',
    'War Eagle Invitational (College Club)',
    'Fall Champs 2018 (College Club)',
    '3rd Annual Twin Cities Invite (College Club)',
    '46th Leatherstocking Swim Meet (USMS)',
    'Sugar Creek Swim Club Pumpkin Paddle Invitational (USMS)',
    'AU vs. Emory University (College Club)',
    '2018 Shark Tank SCM Meet (USMS)',
    'Ottermania 2018 (MSC)',
    'Du It Again',
    'Harvest Hootenanny Biathlon',
    'Las Vegas Kids Triathlon Long',
    'Las Vegas Kids Triathlon Short',
    'Patagonia Lake Triathlon - Olympic Triathlon',
    '2018 Trick or Tri 70.3 Mile',
]


class EventFactory(factory.django.DjangoModelFactory):
    """Fabricate an event with realistic data"""
    class Meta:
        model = Event

    name = factory.LazyAttribute(lambda o: random.choice(event_list))
    event_type = factory.LazyAttribute(lambda o: random.choice(EVENT_TYPE_CHOICES)[0])
    slug = factory.LazyAttribute(lambda o: slugify(o.name))
    start = factory.Faker('date_time_this_century', tzinfo=pytz.UTC)
    address = factory.Faker('address')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    url = factory.Faker('url')
    human = User.objects.all().order_by('?').first()
    organization = Org.objects.all().order_by('?').first()
    fee = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    fee_paid = factory.Faker('pybool')
    notes = factory.Faker('paragraph')
