from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm


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
    description = models.TextField(max_length=1000,blank=True)
    feeling = models.CharField(max_length=20,choices=FEELING,blank=True)
    effort = models.CharField(max_length=20, choices=EFFORT,blank=True)
    notes = models.TextField(max_length=1000,blank=True, verbose_name="post workout notes")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ["date"]
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.date))

    @property
    def get_html_url(self):
        url = reverse('log:workout_edit', args=(self.id,))
        return f'<a href="{url}"><div class="workout {self.workouttype}">' \
               f'<div class="row">' \
               f'<div class="col-xl-2 col-lg-3 text-center">' \
               f'<div class="row icons mt-1">' \
               f'<div class="col-4 ms-1  {self.workouttype}"></div>' \
               f'<div class="col-4 ms-1  {self.feeling}"></div>' \
               f'<div style="font-size: 1.1rem;" class="col-4 mt-n1 effort">{self.effort}</div>' \
               f'</div></div><div class="col-xl-10 col-lg-9">' \
               f'<div class="name">{self.name}</div>' \
               f'<div class="description">{self.description}</div></div></div>' \
               f'</div></a> '

    def get_date(self,year, month, day):
        return f'<a href="../workout/new/{year}-{month}-{day}" class="add"> + </a>'



class WorkoutType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Name of the workout type",
                            help_text='Easy-paced run, Strength training,...')
    icon = models.ImageField(upload_to='icons/', height_field=None, width_field=None, max_length=100, default='')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_icon(self):
        return self.icon

