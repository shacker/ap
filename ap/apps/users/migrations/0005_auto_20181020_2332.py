# Generated by Django 2.1.2 on 2018-10-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_organizations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='organizations',
        ),
        migrations.AddField(
            model_name='user',
            name='ap_organizations',
            field=models.ManyToManyField(blank=True, help_text='Groups or organizations registered on athlete.photo, of which this user is a member.', to='users.Organization'),
        ),
    ]
