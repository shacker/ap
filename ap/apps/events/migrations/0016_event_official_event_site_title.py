# Generated by Django 2.1.2 on 2018-10-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20181027_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='official_event_site_title',
            field=models.CharField(blank=True, help_text='Site title for primary Event page elsewhere on the internet.', max_length=200),
        ),
    ]
