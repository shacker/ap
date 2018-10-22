from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse

from ap.apps.users.forms import ProfileForm
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
    profile = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'profile': profile}, )


def edit_profile(request: HttpRequest) -> HttpResponse:
    """
    User edits own profile
    """
    profile = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            p = form.save(commit=False)
            p.profile_edited = True
            form.save_m2m()
            p.save()

            messages.success(request, "Profile updated successfully")
            return redirect(reverse('users:profile', kwargs={"username": profile.username}))
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_edit.html', {"form": form}, )
