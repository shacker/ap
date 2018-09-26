from allauth.account.models import EmailAddress
from django.contrib import admin

from ap.apps.users.models import Organization, User


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ['organizations', ]


admin.site.register(Organization)
admin.site.register(User, UserAdmin)
admin.site.unregister(EmailAddress)
