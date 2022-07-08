from urllib import request
from django import forms
from . models import *


class AddReview(forms.ModelForm):
    class Meta:
        model = review
        fields = ['message', 'published']