from django.contrib import admin

from ap.apps.events.models import Event, Route


class RouteInline(admin.TabularInline):
    model = Route

class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ['human', 'organization']
    list_display = ['name', 'event_type', 'start', 'fee_paid']
    inlines = [RouteInline, ]


admin.site.register(Event, EventAdmin)
admin.site.register(Route)
