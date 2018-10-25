from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User
from ap.apps.orgs.models import Org

EVENT_TYPE_CHOICES = (
    ('Ride', 'Ride'),
    ('Run', 'Run'),
    ('Swim', 'Swim'),
    ('Triathlon', 'Triathlon'),
    ('Other', 'Other'),
)


# Create your models here.
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

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Human-readable address or location for event meeting place."
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

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return self.name
