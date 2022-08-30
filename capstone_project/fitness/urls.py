from re import template
from django.urls import path
from . import views
#importing default django login/user views -- Rename the views when importing
from django.contrib.auth import views as auth_views 
from users import views as user_views


#URL name changes WILL affect navbar routing
#url patterns use the functions in views.py 
urlpatterns = [
    path('', views.home, name='fitness-home'),
    path('index/', views.home, name='fitness-home'),
    path('workouts/', views.workouts, name='fitness-workouts' ),
    path('leaderboard/', views.leaderboard, name='fitness-leaderboard' ),
    path('profile/', user_views.profile, name='fitness-profile' ),
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='fitness-signin' ),
    path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='fitness-signout' ),
    path('signup/', user_views.signup, name='fitness-signup' ),
]