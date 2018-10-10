from django.db import models

from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User
from ap.apps.events.models import Event


def event_photo_filename(instance, filename):
    return '/'.join(['photos', instance.event.slug, f'{instance.id}_{filename}'])


class Photo(TimeStampedModel):
    """Data definition for a Photo."""

    timestamp = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        help_text="Date/time at which photo was taken."
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to=event_photo_filename,
        max_length=100
    )

    title = models.CharField(
        max_length=100,
        blank=True
    )

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    subject = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="Primary subject of photo"
    )

    def __str__(self):
        """Unicode representation of a Photo."""

        subject = "Unknown"

        if self.subject:
            subject = self.subject.get_full_name()

        return f"{subject} - {self.timestamp}"
