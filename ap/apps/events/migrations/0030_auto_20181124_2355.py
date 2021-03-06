# Generated by Django 2.1.2 on 2018-11-25 07:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0029_auto_20181124_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(blank=True, help_text='Other users on athlete.photo functioning as organizers for this event.', limit_choices_to={'groups__name': 'Organizers'}, related_name='organizer_to_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='photographers',
            field=models.ManyToManyField(blank=True, help_text='Other users on athlete.photo designated as photographers for this event.', limit_choices_to={'groups__name': 'Photographers'}, related_name='photographer_to_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
