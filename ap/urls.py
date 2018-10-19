from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from ap.apps.core import views as coreviews

app_name = 'ap'

urlpatterns = [

    path(
        '',
        coreviews.home,
        name="home"),

    path(
        'faqs/<str:section_title>/',
        coreviews.faqs_section,
        name="faqs_section"),

    path(
        'faqs/',
        coreviews.faqs_index,
        name="faqs_index"),

    path(
        'about/',
        coreviews.about,
        name="about"),


    path('accounts/', include('allauth.urls')),
    path('contact/', include('ap.apps.contact.urls')),
    url(settings.ADMIN_URL, admin.site.urls),
]
