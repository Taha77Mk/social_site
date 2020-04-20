from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Profilep(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'profile_pic']
