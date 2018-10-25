from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static


from ap.apps.core import views as coreviews

app_name = 'ap'

urlpatterns = [

    path(
        '',
        coreviews.home,
        name="home"),

    path(
        'about/',
        coreviews.about,
        name="about"),


    path('accounts/', include('allauth.urls')),
    path('faqs/', include('ap.apps.faqs.urls')),
    path('contact/', include('ap.apps.contact.urls')),
    path('athletes/', include('ap.apps.users.urls')),
    path('events/', include('ap.apps.events.urls')),
    url(settings.ADMIN_URL, admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
