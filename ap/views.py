from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> HttpResponse:
    """Homepage view.
    """
    context = {}
    return render(request, 'ap/home.html', context)
