from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    """FAQs index view
    """

    return render(request, "faqs/index.html")


def section(request, section_title: str) -> HttpResponse:
    """FAQs section view - FAQ lists for participants, organizers, photographers
    """

    ctx = {
        "section_title": section_title,
    }

    return render(request, "faqs/section.html", context=ctx)
