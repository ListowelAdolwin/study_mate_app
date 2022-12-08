from django.forms import ModelForm, widgets
from .models import Room, Profile
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
            'name' : forms.TextInput(attrs={'class':'', 'placeholder':'Enter room name'}),
            'description': forms.Textarea(attrs={'class':'','placeholder':'Write room descripition'}),
            'topic': forms.Select(attrs={'class':''}),
        }

class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']


class  ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'', 'placeholder':'Enter first name'}),
            'last_name' : forms.TextInput(attrs={'class':'', 'placeholder':'Enter last name'}),
            #'avatar': forms.ImageField(),
            'bio': forms.Textarea(attrs={'class':'','placeholder':'Enter bio'}),
        }
