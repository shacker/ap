# Generated by Django 2.1.2 on 2018-11-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_auto_20181123_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='zoom',
            field=models.SmallIntegerField(default=12, help_text='Zoom level for map display'),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=12, help_text='For map display', max_digits=20, null=True),
        ),
    ]