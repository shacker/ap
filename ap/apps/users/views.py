import bleach
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.db.models import Q

from ap.apps.users.forms import ProfileForm
from ap.apps.users.models import User


def users_list(request: HttpRequest) -> HttpResponse:
    """
    Linked list of all or some users for authorized viewers.
    """

    users = User.objects.all()
    paginator = Paginator(users, 100)  # num per page
    page = request.GET.get('page')
    athletes = paginator.get_page(page)
    return render(request, 'users/index.html', {'athletes': athletes}, )


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
        # import pdb; pdb.set_trace()

        if form.is_valid():
            p = form.save(commit=False)
            p.profile_edited = True
            p.about = bleach.clean(form.cleaned_data['about'], strip=True)
            form.save_m2m()
            p.save()

            messages.success(request, "Profile updated successfully")
            return redirect(reverse('users:profile', kwargs={"username": profile.username}))
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/profile_edit.html', {"form": form}, )


def search(request):
    """Display results of search for Athletes (users)
    """

    q = request.GET.get("q") if request.GET.get("q") else None

    if q:
        qs = User.objects.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q) |
            Q(username__icontains=q) |
            Q(about__icontains=q)
        ).order_by("username")
    else:
        qs = User.objects.none()

    paginator = Paginator(qs, 10)
    page = request.GET.get("page")
    items = paginator.get_page(page)

    context = {"items": items, "q": request.GET.get("q")}
    return render(request, "users/search.html", context)
