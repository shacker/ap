from django import forms
from django.contrib.auth.password_validation import validate_password, password_validators_help_texts


class SinglePasswordForm(forms.Form):
    password1 = forms.CharField()

    def clean_password1(self) -> str:
        password1 = self.cleaned_data.get('password1', '')
        if validate_password(password1) is not None:
            raise forms.ValidationError(password_validators_help_texts(), code='pw_invalid')
        return password1
