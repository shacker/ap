from django.contrib import admin

from ap.apps.events.models import Event, Route, Organization


class RouteInline(admin.TabularInline):
    model = Route


class OrgAdmin(admin.ModelAdmin):
    autocomplete_fields = ['human']
    search_fields = ['name', ]
    prepopulated_fields = {"slug": ("name",)}


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start', 'fee_paid']
    inlines = [RouteInline, ]
    filter_horizontal = ['organizations', 'organizers', 'photographers']


admin.site.register(Event, EventAdmin)
admin.site.register(Route)
admin.site.register(Organization, OrgAdmin)
