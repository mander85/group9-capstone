from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm

import fitness #imported for form submission conformation

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
            messages.success(request, f'Account has been created for {username}!')
            return redirect ('fitness-home')
        #error messages when user does not follow form instructions
        else:
            messages.warning(request, f'Please follow all instructions' )
    else:
        form = UserSignupForm()
    return render (request, 'users/signup.html', {'form': form})

def signin(request):
    form = UserSignupForm()
    return render (request, 'users/signin.html', {'form': form})

