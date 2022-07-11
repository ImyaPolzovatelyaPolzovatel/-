from django import forms
from .models import *
from captcha.fields import CaptchaField


class ContactsForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contacts
        fields = '__all__'
