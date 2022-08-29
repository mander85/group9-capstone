from django.urls import path
from . import views
from users import views as user_views


#URL name changes WILL affect navbar routing
#url patterns use the functions in views.py 
urlpatterns = [
    path('', views.home, name='fitness-home'),
    path('index/', views.home, name='fitness-home'),
    path('workouts/', views.workouts, name='fitness-workouts' ),
    path('leaderboard/', views.leaderboard, name='fitness-leaderboard' ),
    path('profile/', views.profile, name='fitness-profile' ),
    path('signin/', user_views.signin, name='fitness-signin' ),
    path('signup/', user_views.signup, name='fitness-signup' ),
]