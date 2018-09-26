from django.contrib import admin

from allauth.account.models import EmailAddress

from ap.apps.users.models import User

admin.site.register(User)
admin.site.unregister(EmailAddress)
