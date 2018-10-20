from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> HttpResponse:
    """Homepage view
    """

    return render(request, 'core/home.html')


def about(request) -> HttpResponse:
    """About this site
    """

    return render(request, "core/about.html")
