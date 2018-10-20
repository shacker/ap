from django.urls import path

from ap.apps.faqs import views

app_name = 'faqs'

urlpatterns = [

    path(
        '<str:section_title>/',
        views.section,
        name="section"),

    path(
        '',
        views.index,
        name="index"),
]
