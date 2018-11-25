# Generated by Django 2.1.2 on 2018-11-25 07:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20181124_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='official_event_site_url',
            field=models.URLField(blank=True, help_text='URL for primary Event page elsewhere on the internet', null=True, verbose_name='External Event Website URL'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(blank=True, help_text='Other users on athlete.photo functioning as organizers for this event.', related_name='event_organizers', to=settings.AUTH_USER_MODEL),
        ),
    ]
