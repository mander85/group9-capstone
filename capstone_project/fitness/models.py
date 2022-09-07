
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

# Creating the database table for leaderboard entries
#Table Defunct, kept in case of reuse later
#class Leader_Post(models.Model):
#    reps = models.IntegerField()
#    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
#    def __str__(self):
#        return str(self.submitter) + " " + str(self.reps)

class Leader_Post_bytime(models.Model):
    time = models.IntegerField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.submitter) + " " + str(self.time)
