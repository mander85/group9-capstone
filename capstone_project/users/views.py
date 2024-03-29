
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserSignupForm, PasswordChangeForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserChangeForm




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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been successfully updated!')
            return redirect ('profile')
    else: 
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')

#The view to allow users to change their own password with current password
def change_password(request):
    if request.method == 'POST':
        user = request.user
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been updated!")
            return redirect('password_reset')
        else:
            messages.error(request, 'Please correct the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_reset.html',
        {'form':form}
    )

def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        form = UserChangeForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Success message")
            return redirect('edit_profile')
        else:
            messages.error(request, 'Error Message')
    else:
        form = UserChangeForm(request.user)
    return render(request, 'users/edit_profile.html',
        {'form':form}
    )
