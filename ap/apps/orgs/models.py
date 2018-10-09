from django.db import models

from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from ap.apps.users.models import User


class Org(TimeStampedModel):
    """Data definition for an Organization."""

    name = models.CharField(
        max_length=100
    )

    slug = AutoSlugField(
        populate_from='name'
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

    class Meta:
        """Meta definition for Organization."""

        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    def __str__(self):
        """Unicode representation of Organization."""
        return self.name
