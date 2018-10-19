from django.urls import path

from ap.apps.contact import views

app_name = 'contact'

urlpatterns = [

    path(
        '',
        view=views.contact,
        name='contact'
    ),
    path(
        'success/',
        view=views.success,
        name='success'
    ),
]
