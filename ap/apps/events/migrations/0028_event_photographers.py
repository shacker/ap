# Generated by Django 2.1.2 on 2018-11-25 07:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0027_auto_20181124_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photographers',
            field=models.ManyToManyField(blank=True, help_text='Other users on athlete.photo designated as photographers for this event.', limit_choices_to={'groups__name': 'Photographers'}, related_name='event_photographers', to=settings.AUTH_USER_MODEL),
        ),
    ]
