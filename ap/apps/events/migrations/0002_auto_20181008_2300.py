# Generated by Django 2.1.1 on 2018-10-09 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # ('orgs', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='ap_contact',
        ),
        migrations.AddField(
            model_name='event',
            name='human',
            field=models.ForeignKey(blank=True, help_text='Another user on athlete.photo functioning as a contact for this event.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Human Contact'),
        ),
        # migrations.AddField(
        #     model_name='event',
        #     name='organization',
        #     field=models.ForeignKey(blank=True, help_text='An organization registered on athlete.photo representing the overall host for this event.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.Org', verbose_name='Organization'),
        # ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=140),
        ),
    ]
