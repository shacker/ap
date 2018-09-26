from django.urls import path

from ap.apps.users import views

app_name = 'users'

urlpatterns = [

    path(
        'list/',
        view=views.users_list,
        name='list'
    ),
]
