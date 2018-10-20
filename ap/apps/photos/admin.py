from django.contrib import admin

from ap.apps.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'timestamp',
        'title'
    )

admin.site.register(Photo, PhotoAdmin)
