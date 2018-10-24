from django.contrib import admin

from ap.apps.events.models import Event

class EventAdmin(admin.ModelAdmin):
    autocomplete_fields = ['human', 'organization']


admin.site.register(Event, EventAdmin)
