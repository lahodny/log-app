from django.forms import ModelForm

from log.models import Workout


class WorkoutModelForm(ModelForm):
    class Meta:
        model = Workout
        #fields = ['name', 'date','workouttype']
