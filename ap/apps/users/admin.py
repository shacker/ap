from allauth.account.models import EmailAddress
from django.contrib import admin

from ap.apps.users.models import User
# from ap.apps.orgs.models import Org


class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'first_name', 'last_name', ]
    filter_horizontal = ['ap_organizations', ]
    list_display = ['username', 'usergroups']
    list_filter = ('groups', )

    def usergroups(self, obj):
        return ([obj.name for obj in obj.groups.all()])
    usergroups.short_description = 'Groups'


admin.site.register(User, UserAdmin)
admin.site.unregister(EmailAddress)
