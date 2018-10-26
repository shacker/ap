from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User
from ap.apps.orgs.models import Org
from ap.apps.users.constants import COUNTRY_CHOICES


EVENT_TYPE_CHOICES = (
    ('Ride', 'Ride'),
    ('Run', 'Run'),
    ('Swim', 'Swim'),
    ('Triathlon', 'Triathlon'),
    ('Other', 'Other'),
)


class Event(TimeStampedModel):
    """Data definition for an athletic Event."""

    name = models.CharField(
        max_length=140
    )

    slug = AutoSlugField(
        populate_from='name'
    )

    event_type = models.CharField(
        max_length=12,
        default='Other',
        choices=EVENT_TYPE_CHOICES
    )

    start = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        help_text="Date and time for start of event."
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
        max_length=255,
        blank=True,
        null=True,
        help_text="Street address/location for event meeting place. Do not include city/state/country."
    )

    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=12,
        blank=True,
        null=True,
        help_text="For map display"
    )

    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=12,
        blank=True,
        null=True,
        help_text="For map display"
    )

    url = models.URLField(
        blank=True,
        null=True,
        max_length=200,
        help_text="URL for primary Event page elsewhere on the internet."
    )

    human = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Human Contact",
        help_text="Another user on athlete.photo functioning as a contact for this event."
    )

    organization = models.ForeignKey(
        Org,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Organization",
        help_text="An organization registered on athlete.photo representing the overall host for this event."
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
        help_text="Ready for public display (defaults to False)"
    )

    objects = models.Manager()

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return self.name


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
