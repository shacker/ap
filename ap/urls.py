from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from ap import views

app_name = 'ap'

urlpatterns = [

    path(
        '',
        views.home,
        name="home"),

    path('accounts/', include('allauth.urls')),
    url(settings.ADMIN_URL, admin.site.urls),
]
