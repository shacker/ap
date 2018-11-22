from django.urls import path

from ap.apps.events import views

app_name = 'events'

urlpatterns = [

    path(
        'search/',
        views.search,
        name="search"),

    path(
        '<int:event_id>/<str:event_slug>/organize/',
        views.organize_event,
        name="organize_event"),

    path(
        '<int:event_id>/<str:event_slug>/',
        views.detail,
        name="detail"),

    path(
        'organize/',
        views.index,
        {'organize': True},
        name="organizers_index"
    ),

    path(
        '<str:tense>/',
        views.index,
        name="index"),

    path(
        '',
        views.index,
        name="index"),
]
