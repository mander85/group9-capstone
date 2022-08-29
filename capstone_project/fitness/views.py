from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#views allow for navigation across the webpage using the templates in capstone_project/fitness/templates
def home(request):
    return render(request, 'fitness/index.html') 

def workouts(request):
    return render(request, 'fitness/workouts.html')

def leaderboard(request):
    return render(request, 'fitness/leaderboard.html')

def profile(request):
    return render(request, 'fitness/profile.html')

def signinup(request):
    return render(request, 'fitness/signinup.html')

    
