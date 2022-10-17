from socket import fromshare
#imports to allow changes to default Django forms to allow users to enter their email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    #Meta class is a nested space for keeping configs in one place.
    class Meta: 
        #when this form validates it creates a new user - the model being affected
        model = User
        #what is shown on our form and the order they are shown in
        fields = ['username', 'email', 'password1', 'password2']





