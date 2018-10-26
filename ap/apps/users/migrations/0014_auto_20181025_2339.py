# Generated by Django 2.1.2 on 2018-10-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20181022_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='state_provenance',
        ),
        migrations.AddField(
            model_name='user',
            name='state_province',
            field=models.CharField(blank=True, help_text='Name of your state or province', max_length=100, verbose_name='State or Province'),
        ),
    ]