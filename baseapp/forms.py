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
    #avatar = forms.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
