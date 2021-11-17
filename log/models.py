from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    FEELING = [
        ('GREAT', 'Great'),
        ('GOOD', 'Good'),
        ('NORMAL', 'Normal'),
        ('POOR', 'Poor'),
        ('TERRIBLE', 'Terrible'),
    ]
    EFFORT = [
        ('1', 'Very light'),
        ('2', 'Light'),
        ('3', 'Light'),
        ('4', 'Moderate'),
        ('5', 'Moderate'),
        ('6', 'Moderate'),
        ('7', 'Hard'),
        ('8', 'Hard'),
        ('9', 'Very hard'),
        ('10', 'Max effort'),
    ]

    date = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.") #tady bude default brany z UI
    time = models.TimeField(null=True,blank=True)
    workouttype = models.ForeignKey('WorkoutType',on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    feeling = models.CharField(max_length=20,choices=FEELING,blank=True)
    effort = models.CharField(max_length=20, choices=EFFORT,blank=True)
    notes = models.TextField(blank=True, verbose_name="post workout notes")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["date"]
    def __str__(self):

        return self.name

class WorkoutType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name of the workout type",
                            help_text='Easy-paced run, Strength training,...')
    class Meta:
        ordering = ["name"]

    def __str__(self):

        return self.name