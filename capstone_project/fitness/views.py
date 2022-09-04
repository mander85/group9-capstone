from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Leader_Post


# Create your views here.

#views allow for navigation across the webpage using the templates in capstone_project/fitness/templates
def home(request):
    return render(request, 'fitness/index.html') 

@login_required
def workouts(request):
    return render(request, 'fitness/workouts.html')

@login_required
def leaderboard(request):
    #this posts sorts the table in high to low order by reps and returns it
    posts=Leader_Post.objects.order_by('-reps')
    context= {'posts': posts}
    return render(request, 'fitness/leaderboard.html', context)
  




    
