from cms.models import User
from django.forms import ModelForm
from django import forms

from log import models
from log.models import Workout


#class WorkoutModelForm(ModelForm):
#    class Meta:
#        model = Workout
        #fields = ['name', 'date','workouttype']


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ('date','time','workouttype','name','description','feeling','effort','notes')
    """name = forms.CharField()

    def name(self):
        data = self.name['name']
        return data"""