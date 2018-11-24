from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User
# from ap.apps.orgs.models import Org
from ap.apps.users.constants import COUNTRY_CHOICES


EVENT_TYPE_CHOICES = (
    ('roadbike', 'Cycling'),
    ('hike', 'Hike'),
    ('mtb', 'Mountain Bike'),
    ('run', 'Run'),
    ('swim', 'Swim'),
    ('tri', 'Triathlon'),
    ('other', 'Other'),
)


class Organization(TimeStampedModel):
    """Data definition for an Organization."""

    name = models.CharField(
        max_length=100
    )

    slug = models.SlugField(
        help_text="Shortened version of organization name for use in URLs"
    )

    address = models.CharField(
        max_length=255,
        blank=True,
    )

    phone = models.CharField(
        max_length=64,
        blank=True,
    )

    email = models.EmailField(
        max_length=254,
        blank=True,
    )

    human = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    objects = models.Manager()

    class Meta:
        """Meta definition for Organization."""

        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        """Unicode representation of Organization."""
        return self.name


class Event(TimeStampedModel):
    """Data definition for an athletic Event."""

    title = models.CharField(
        max_length=140,
        verbose_name="Event Title"
    )

    slug = AutoSlugField(
        populate_from='name'
    )

    event_type = models.CharField(
        max_length=12,
        default='other',
        choices=EVENT_TYPE_CHOICES
    )

    about = models.TextField(
        blank=True,
        help_text="Brief description of this event. Plain text only."
    )

    start = models.DateTimeField(
        verbose_name="Start Date and Time",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        help_text="Date and time for start of event."
    )

    place_name = models.CharField(
        verbose_name="Start Place Name",
        max_length=100,
        blank=True,
        help_text="Name of the site, building, or area where event begins."
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="City or town for event meeting place."
    )

    state_province = models.CharField(
        'State or Province',
        blank=True,
        max_length=100,
        help_text="State, region, or province for event meeting place"
    )

    country = models.CharField(
        blank=True,
        max_length=64,
        choices=COUNTRY_CHOICES)

    address = models.CharField(
        verbose_name="Start Place Address",
        max_length=255,
        blank=True,
        null=True,
        help_text="Street address/location for event meeting place. Do not include city/state/country."
    )

    latitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        blank=True,
        null=True,
        help_text="For map display"
    )

    longitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        blank=True,
        null=True,
        help_text="For map display"
    )

    zoom = models.SmallIntegerField(
        default=12,
        help_text="Zoom level for map display"
    )

    official_event_site_url = models.URLField(
        verbose_name="External Event Website URL",
        blank=True,
        null=True,
        max_length=200,
        help_text="URL for primary Event page (can be elsewhere on the internet)"
    )

    official_event_site_title = models.CharField(
        verbose_name="External Event Website Title",
        blank=True,
        max_length=200,
        help_text="Site title for primary Event page. Will be linked to External Event Website URL."
    )

    organizers = models.ManyToManyField(
        User,
        blank=True,
        help_text="Other users on athlete.photo functioning as organizers for this event."
    )

    organizations = models.ManyToManyField(
        Organization,
        blank=True,
        help_text="One or more organizations that sponsor or support this event"
    )

    fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        help_text="Platform fee paid by Event organizer to athlete.photo"
    )

    fee_paid = models.BooleanField(
        default=False,
        help_text="Event fee has been paid in full"
    )

    notes = models.TextField(
        'Internal Notes',
        blank=True,
        help_text="Internal/private notes regarding the event. For use by athlete.photo only."
    )

    published = models.BooleanField(
        default=False,
        help_text="Unpublished events are hidden from public display."
    )

    objects = models.Manager()

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return self.title


class Route(TimeStampedModel):
    '''Links to route pages at Strava, MapMyRide, RideWithGPS, etc.
    Unlimited number of route links per event.'''

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=140,
        help_text="e.g. \"Albany Fun Run 13\" or \"Morro Bay Lighthouse Century 2018\""
    )

    url = models.URLField(
        "URL",
        max_length=200,
        help_text="Link to route page at Strava, MapMyRide, RideWithGPS, etc."
    )

    def __str__(self):
        """Unicode representation of Route."""
        return f"Route for {self.title}"
