from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from ap.apps.users.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'about',
            'avatar',
            'personal_website',
            'professional_website',
            'facebook',
            'instagram',
            'twitter',
            'linkedin',
            'ap_organizations',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update Profile'))
