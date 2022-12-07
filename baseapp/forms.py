from django.forms import ModelForm, widgets
from .models import Room
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control room-form', 'placeholder':'Enter room name'}),
            'description': forms.Textarea(attrs={'class':'form-control room-form','placeholder':'Write room descripition'}),
            'topic': forms.Select(attrs={'class':'form-control room-form'}),
        }

class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
"""
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control room-form', 'placeholder':'Enter your first name'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control room-form', 'placeholder':'Enter your last name'}),
            'username' : forms.TextInput(attrs={'class':'form-control room-form', 'placeholder':'Enter your username'}),
            'email' : forms.EmailField(attrs={'class':'form-control room-form', 'placeholder':'Enter your email'}),

            'password1': forms.PasswordInput(attrs={'class':'form-control room-form','placeholder':'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control room-form', 'placeholder':'Confirm password'}),
        }
 """
