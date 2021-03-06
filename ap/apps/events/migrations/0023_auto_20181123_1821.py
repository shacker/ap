# Generated by Django 2.1.2 on 2018-11-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20181122_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.SmallIntegerField(default=12, help_text='Zoom level for map display'),
        ),
        migrations.AlterField(
            model_name='event',
            name='official_event_site_title',
            field=models.CharField(blank=True, help_text='Site title for primary Event page. Will be linked to Official Event Site URL.', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='official_event_site_url',
            field=models.URLField(blank=True, help_text='URL for primary Event page (can be elsewhere on the internet)', null=True),
        ),
    ]
