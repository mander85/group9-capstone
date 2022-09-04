from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Leader_Post
from .forms import LeaderboardForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

#views allow for navigation across the webpage using the templates in capstone_project/fitness/templates
def home(request):
    return render(request, 'fitness/index.html') 

@login_required
def workouts(request):
    return render(request, 'fitness/workouts.html')

@login_required
def leaderboard(request):
    form = LeaderboardForm
    #handles the form submission 
    if request.method == "POST":
        form = LeaderboardForm(request.POST)
        if form.is_valid():
            #allows the user to enter reps without having to select their username
            leaderpost = form.save(commit=False)
            leaderpost.submitter = request.user
            form.save()
            messages.success(request, f'Reps submitted!')
            return redirect ('fitness-leaderboard')
        else:
            messages.warning(request, f'Please enter your reps' )
    #if the user has not submitted the form
    else:
        #provides the leaderboard data sorted from high to low by reps
        posts=Leader_Post.objects.order_by('-reps')
        return render(request, 'fitness/leaderboard.html', {'form': form, 'posts': posts})





    
