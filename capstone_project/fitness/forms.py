import imp
from django import forms
from django.forms import ModelForm
from .models import Leader_Post

#create a form for users to input reps
class LeaderboardForm(ModelForm):
    class Meta:
        model = Leader_Post
        #the fields users can submit
        fields = ['reps']


