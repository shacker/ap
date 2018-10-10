from django.contrib import admin

from ap.apps.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'subject',
        'title'
    )


admin.site.register(Photo, PhotoAdmin)
