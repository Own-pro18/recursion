from django.db import models

# Create your models here.
class Dt_survey(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=200)

class event(models.Model):
    event_name = models.CharField(max_length=200)
    Venue = models.CharField(max_length=200)
    organizer = models.CharField(max_length=200)
    Date = models.DateTimeField('date published')