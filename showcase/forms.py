from django import forms
from django.contrib.auth.models import User

from .models import Work


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['image','linkTo','title', 'description']
