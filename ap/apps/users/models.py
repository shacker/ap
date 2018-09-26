from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class Organization(models.Model):
    """
    External group or organization of which user is a member.
    """

    name = models.CharField(
        max_length=128
    )
    org_link = models.URLField(
        blank=True,
        help_text="Used to link back to the organization's homepage (or to any URL)."
    )

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    '''
    Inherits all native User fields from Django auth.User model and allows adding custom fields
    (no need for separate Profile model).
    https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#user-model
    '''

    organizations = models.ManyToManyField(
        Organization,
        help_text="Groups or organizations of which this user is a member.",
        blank=True)

    class Meta:
        app_label = 'users'

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self) -> str:
        return reverse('users:detail', kwargs={'username': self.username})
