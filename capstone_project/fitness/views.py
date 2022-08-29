from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#some dummy data
#    posts = [
#        {
#            'author': 'Miranda A',
#            'title': 'blog post 1',
#            'content': 'first post',
#            'date_posted': 'august 27, 2022'
#        },
#        {
#            'author': 'Miranda B',
#            'title': 'blog post 2',
#            'content': 'second post',
#            'date_posted': 'august 28, 2022'
#        },
#    ]
def home(request):
    #test stuff from the tutorial
    #context = {
    #    'posts': posts
    #}
    return render(request, 'fitness/index.html') # context)

def workouts(request):
    return render(request, 'fitness/workouts.html')

def leaderboard(request):
    return render(request, 'fitness/leaderboard.html')

def profile(request):
    return render(request, 'fitness/profile.html')

def signinup(request):
    return render(request, 'fitness/signinup.html')

    
