from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User


# Create your models here.
class Event(TimeStampedModel):
    """Data definition for an athletic Event."""

    name = models.CharField(
        max_length=100)

    slug = AutoSlugField(
        populate_from='name')

    start = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
        help_text="Date and time for start of event.")

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Human-readable address or location for event meeting place.")

    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=12,
        blank=True,
        null=True,
        help_text="For map display")

    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=12,
        blank=True,
        null=True,
        help_text="For map display")

    url = models.URLField(
        blank=True,
        null=True,
        max_length=200,
        help_text="URL for primary Event page elsewhere on the internet.")

    ap_contact = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="AP Contact",
        help_text="Another user on athlete.photo functioning as a contact for this event.")

    class Meta:
        """Meta definition for Event."""

        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        """Unicode representation of Event."""
        return self.name
