from django.urls import path

from ap.apps.users import views

app_name = 'users'

urlpatterns = [

    path(
        '',
        view=views.users_list,
        name='list'
    ),

    path(
        '<str:username>/',
        view=views.profile,
        name='profile'
    ),
]
