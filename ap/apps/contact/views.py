import bleach

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, reverse

from .forms import ContactForm


def contact(request):
    """Primary contact form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = bleach.clean(form.cleaned_data['subject'], strip=True)
            message = bleach.clean(form.cleaned_data['message'], strip=True)

            try:
                send_mail(subject, message, from_email, settings.ADMINS)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('contact:success'))

    return render(request, "contact/contact.html", {'form': form})


def success(request):
    return render(request, "contact/success.html")
