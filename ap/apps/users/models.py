from typing import Any

from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models

from ap.apps.users.constants import COUNTRY_CHOICES



def get_avatar_upload_dir(instance: Any, filename: str) -> str:
    """Determine upload dir for avatar image files
    """
    return '/'.join(['avatars', instance.username, filename])



class User(AbstractUser):
    '''
    Inherits all native User fields from Django auth.User model and allows adding custom fields
    (no need for separate Profile model).
    https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#user-model
    '''

    about = models.TextField(
        help_text="A few sentences about you. Plain text only, no formatting.",
        blank=True
    )

    city = models.CharField(
        blank=True,
        max_length=100,
        help_text="Name of your city"
    )

    state_provenance = models.CharField(
        'State or Provenance',
        blank=True,
        max_length=100,
        help_text="Name of your state or provenance"
    )

    country = models.CharField(
        blank=True,
        max_length=64,
        choices=COUNTRY_CHOICES)

    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to=get_avatar_upload_dir,
        help_text="An image of you, to be used with your profile."
    )

    email = models.EmailField(
        max_length=254,
        blank=True,
        help_text="We will never display your email on the website."
    )

    personal_website = models.URLField(
        max_length=200,
        blank=True,
        help_text="Your blog, profile, or hobby website or page URL."
    )

    professional_website = models.URLField(
        max_length=200,
        blank=True,
        help_text="Your work-related website or profile page URL."
    )

    facebook = models.CharField(
        blank=True,
        max_length=100,
        help_text="Your Facebook username (not URL)."
    )

    instagram = models.CharField(
        blank=True,
        max_length=100,
        help_text="Your Instagram username (not URL)."
    )

    twitter = models.CharField(
        blank=True,
        max_length=100,
        help_text="Your Twitter username (not URL)."
    )

    linkedin = models.CharField(
        blank=True,
        max_length=100,
        verbose_name="LinkedIn",
        help_text="Your LinkedIn username (not URL)."
    )

    ap_organizations = models.ManyToManyField(
        'orgs.Org',
        blank=True,
        verbose_name="AP Orgs",
        help_text="Groups or organizations registered on athlete.photo, of which this user is a member.",
    )

    profile_edited = models.BooleanField(
        default=False,
        help_text="Alert user if they have never set up their profile"
    )

    class Meta:
        app_label = 'users'

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self) -> str:
        return reverse('users:detail', kwargs={'username': self.username})
