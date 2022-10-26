
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

import datetime


#### This is the table for the leaderboard posts
# time is the time worked out that is submitted by the user
# submitter is the username of the person submitting the form - no form field for it 
# the date posted is taken at time of form submission, the database entry for it is able to be edited by admin
# Users can still make multiple posts
class Leader_Post_bytime(models.Model):
    time = models.IntegerField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=datetime.date.today)
    def __str__(self):
        return str(self.submitter) + " " + str(self.time) + " " + str(self.date_posted) 

# The database table for the workout generator
class Generator_Exercises(models.Model):
    exercise_id = models.IntegerField()
    exercise_name = models.CharField(max_length=120)
    exercise_duration = models.CharField(max_length=120)

    def __str__(self):
        return str(self.exercise_id) + " " + str(self.exercise_name)