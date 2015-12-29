from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Venue(models.Model):
    venue_Name = models.CharField(max_length=45)
    venue_Location = models.CharField(max_length=45)
    venue_Description = models.CharField(max_length=250)
    venue_Category = models.CharField(max_length=15)
    venue_Rating = models.IntegerField(null=True)
    venue_Site = models.CharField(max_length=45, null=True)
    venue_Logo = models.CharField(max_length=45, null=True)
    venue_Updated = models.DateTimeField('date published')
    venue_Owner = models.ForeignKey(User)
    def __str__(self):              # __unicode__ on Python 2
        return self.venue_Name

class CinemaLocs(models.Model):
    location = models.CharField(max_length=45)
    def __str__(self):              # __unicode__ on Python 2
        return self.location


