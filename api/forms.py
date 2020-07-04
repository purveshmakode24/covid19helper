from django import forms
from django.contrib.auth.models import User
from .models import *

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['category', 'country', 'city', 'name', 'description']