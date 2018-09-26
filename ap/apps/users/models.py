from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class User(AbstractUser):
    '''
    Inherits all native User fields from Django auth.User model and allows adding custom fields
    (no need for separate Profile model).
    https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#user-model
    '''

    organization = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        choices=[],
        help_text="Affilation",)

    class Meta:
        app_label = 'users'

    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self) -> str:
        return reverse('users:detail', kwargs={'username': self.username})
