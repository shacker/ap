from django import forms
from django.conf import settings

from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = ReCaptchaField()

    # Enable submission from non-https localhost. Hopefully a temp workaround.
    # https://github.com/praekelt/django-recaptcha/issues/157
    if getattr(settings, 'DEBUG', False):
        captcha.clean = lambda x: x[0]
