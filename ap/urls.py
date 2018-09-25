from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

from django.conf import settings

from ap import views

app_name = 'ap'

urlpatterns = [

    path(
        '',
        views.home,
        name="home"),

    url(settings.ADMIN_URL, admin.site.urls),

]


