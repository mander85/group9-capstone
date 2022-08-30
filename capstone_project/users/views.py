import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm



#user registration form is supplied by Django framework 
#These views are imported into fitness/urls.py

def signup(request):
    #check for POST request for form validation 
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        #if there is a form submitted and it is valid, then this will grab the username, and be stored as clean data
        if form.is_valid():
            #saves the user into the database
            form.save()
            #lets the user know their creation was successful
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}! Login here')
            return redirect ('fitness-signin')
        #error messages when user does not follow form instructions
        else:
            messages.warning(request, f'Please follow all instructions' )
    else:
        form = UserSignupForm()
    return render (request, 'users/signup.html', {'form': form})

#profile has been moved to users views from fitness views because it deals with user logic
@login_required
def profile(request):
    return render(request, 'users/profile.html')

#def signin(request):
#    form = UserSignupForm()
#    return render (request, 'users/signin.html', {'form': form})

