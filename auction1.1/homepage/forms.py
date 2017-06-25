from django.contrib.auth.models import User
from django import forms


class uform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'cpassword']

