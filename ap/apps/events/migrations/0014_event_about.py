# Generated by Django 2.1.2 on 2018-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20181026_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='about',
            field=models.TextField(blank=True, help_text='Brief description of this event. Plain text only.'),
        ),
    ]
