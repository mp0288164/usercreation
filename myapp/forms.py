# forms.py
from django import forms
from .models import UserRegistration

class UserForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
