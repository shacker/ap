# Generated by Django 2.1.1 on 2018-09-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(blank=True, help_text='Groups or organizations of which this user is a member.', to='users.Organization'),
        ),
    ]
