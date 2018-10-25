from django.contrib import admin

from ap.apps.events.models import Event


class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ['human', 'organization']
    list_display = ['name', 'event_type', 'start', 'fee_paid']


admin.site.register(Event, EventAdmin)
