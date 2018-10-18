from django.shortcuts import render
from django.http import HttpResponse


def home(request) -> HttpResponse:
    """Homepage view
    """

    return render(request, 'core/home.html')


def faqs_index(request) -> HttpResponse:
    """FAQs index view
    """

    return render(request, "core/faqs_index.html")


def faqs_section(request, section_title: str) -> HttpResponse:
    """FAQs section view - FAQ lists for participants, organizers, photographers
    """

    ctx = {
        "section_title": section_title,
    }

    return render(request, "core/faqs_section.html", context=ctx)


def about(request) -> HttpResponse:
    """About this site
    """

    return render(request, "core/about.html")
