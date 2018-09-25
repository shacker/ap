from django.urls import path

from iris.apps.users import views

app_name = 'users'

urlpatterns = [

    path(
        'list/',
        view=views.users_list,
        name='list'
    ),
    path(
        'become/<str:newusername>/',
        view=views.become_user,
        name='become_user'
    ),


]
