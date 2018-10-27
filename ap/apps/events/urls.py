from django.urls import path

from ap.apps.events import views

app_name = 'events'

urlpatterns = [

    path(
        '<int:event_id>/<str:event_slug>/',
        views.detail,
        name="detail"),

    path(
        '<str:tense>/',
        views.index,
        name="index"),

    path(
        '',
        views.index,
        name="index"),
]
