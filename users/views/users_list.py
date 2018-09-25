from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from iris.apps.users.models import User


def users_list(request: HttpRequest) -> HttpResponse:
    """
    Linked list of all or some users for authorized viewers.
    """

    # FIXME: Show a subset for authorized non-sysadmins
    user_list = User.objects.all()
    return render(request, 'users/list.html', {'user_list': user_list}, )
