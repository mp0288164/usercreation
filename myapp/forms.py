# forms.py
from django import forms
from .models import UserRegistration

class UserForm(forms.ModelForm):
    email=forms.EmailField(label='Email-id')
    password=forms.CharField(widget=forms.PasswordInput,label='Password')
    confirm_password=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model = UserRegistration
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data["confirm_password"]

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        
