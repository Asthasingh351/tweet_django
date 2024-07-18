from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Tweetforms(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [ 'text' , 'photo']

class UserRegistrationForm(UserCreationForm):
     email = forms.EmailField()   

class Meta: User
model = User
fields = ('username', 'email', 'password1', 'password2')