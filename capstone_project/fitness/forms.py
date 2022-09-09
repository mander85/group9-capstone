
from django import forms
from django.forms import ModelForm
from .models import Leader_Post_bytime
#from .models import Leader_Post

#create a form for users to input reps ## Defunct 
#class LeaderboardForm(ModelForm):
#   class Meta:
#        model = Leader_Post
#        #the fields users can submit
##        fields = ['reps']

#create a form for users to input time
class LeaderboardForm_bytime(ModelForm):
    class Meta:
        model = Leader_Post_bytime
        #the fields users can submit
        fields = ['time']




