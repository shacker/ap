# Generated by Django 2.1.2 on 2018-10-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False, help_text='Ready for public display (defaults to False)'),
        ),
    ]