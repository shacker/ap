from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from ap.apps.users.models import User


def users_list(request: HttpRequest) -> HttpResponse:
    """
    Linked list of all or some users for authorized viewers.
    """

    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users}, )


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    User detail/profile
    """
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user}, )
