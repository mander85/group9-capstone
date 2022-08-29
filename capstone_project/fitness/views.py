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

#These views were removed -- views are in the user file
#def signin(request):
   #return render(request, 'users/signin.html')

#def signup(request):
    #return render(request, 'users/signup.html')

    
