
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import  Generator_Exercises, Leader_Post_bytime #,Leader_Post
from .forms import LeaderboardForm_bytime #, LeaderboardForm
from django.contrib import messages
#from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

#views allow for navigation across the webpage using the templates in capstone_project/fitness/templates
def home(request):
    return render(request, 'fitness/index.html') 

@login_required
def workouts(request):
    #Generates 10 random workouts from the table -- resource heavy method
    workouts = Generator_Exercises.objects.order_by('?')[:10]
    return render(request, 'fitness/workouts.html', {'workouts': workouts})

@login_required
def leaderboard(request):
    posts=Leader_Post_bytime.objects.order_by('-time')
    page = request.GET.get('page',1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    form = LeaderboardForm_bytime
    #handles the form submission 
    if request.method == "POST":
        form = LeaderboardForm_bytime(request.POST)
        if form.is_valid():
            #allows the user to enter time without having to select their username
            leaderpost = form.save(commit=False)
            leaderpost.submitter = request.user
            form.save()
            messages.success(request, f'Thanks { leaderpost.submitter }! Your time is submitted!')
            return redirect ('fitness-leaderboard')
        else:
            messages.warning(request, f'Please enter your time' )

    #if the user has not submitted the form
    else:
        #provides the leaderboard data sorted from high to low by time
        
        return render(request, 'fitness/leaderboard.html', {'posts': posts,'form': form })


