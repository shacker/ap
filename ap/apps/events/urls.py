from django.urls import path

from ap.apps.events import views

app_name = 'events'

urlpatterns = [

    # path(
    #     '<str:section_title>/',
    #     views.section,
    #     name="section"),

    path(
        '<str:tense>/',
        views.index,
        name="index"),

    path(
        '',
        views.index,
        name="index"),
]
