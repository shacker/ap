
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from ap.users.models import User


def user_detail(request: HttpRequest, username: str) -> HttpResponse:
    """
    Detail view for a single user.
    """

    user = get_object_or_404(User, username=username)
    return render(
        request,
        'users/detail.html',
        {'user': user}
    )
