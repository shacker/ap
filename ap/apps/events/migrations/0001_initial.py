# Generated by Django 2.1.1 on 2018-09-27 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('start', models.DateTimeField(blank=True, help_text='Date and time for start of event.', null=True)),
                ('address', models.CharField(blank=True, help_text='Human-readable address or location for event meeting place.', max_length=255, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=12, help_text='For map display', max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=12, help_text='For map display', max_digits=20, null=True)),
                ('url', models.URLField(blank=True, help_text='URL for primary Event page elsewhere on the internet.', null=True)),
                ('ap_contact', models.ForeignKey(blank=True, help_text='Another user on athlete.photo functioning as a contact for this event.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='AP Contact')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
    ]
