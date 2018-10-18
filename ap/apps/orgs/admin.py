from django.contrib import admin

from ap.apps.orgs.models import Org


class OrgAdmin(admin.ModelAdmin):
    autocomplete_fields = ['human']


admin.site.register(Org, OrgAdmin)
