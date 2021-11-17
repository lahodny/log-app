from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from accounts import models
from log.forms import WorkoutForm
from log.models import Workout, WorkoutType
from django.contrib.auth.decorators import login_required
from django import forms

def index(request):
    """Metoda připravuje pohled pro domovskou stránku - šablona index.html"""

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    workouts = Workout.objects.order_by('-date')

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'workouts': workouts
    }

    """ Pomocí metody render vyrendrujeme šablonu index.html a předáme ji hodnoty v proměnné context k zobrazení """
    return render(request, 'index.html', context=context)


def create(request):

    form = WorkoutForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()

            return HttpResponseRedirect('/log/workouts')
            #Workout.user = request.user
        else:
            form = WorkoutForm
    return render(request, 'log/workout_form.html', {'form': form})




class WorkoutListView(LoginRequiredMixin, generic.ListView):
    model = Workout
    context_object_name = 'workouts_list'

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkoutDetailView(LoginRequiredMixin, generic.DetailView):
    model = Workout

"""
class WorkoutCreateView(LoginRequiredMixin, forms.Form):
    #model = Workout
    #fields = ['date','time','workouttype','name','description','feeling','effort','notes','user']
    #success_url = reverse_lazy('workouts')
    #login_url = '/accounts/login/'
    def create(self, request):
        #user = models.Client.objects.get(user=self)
        if request.method == 'POST':
            form = forms.WorkoutModelForm(request.POST)
            if form.is_valid():
                Workout.user = request.user
        else:
            form = forms.WorkoutModelForm()
        return render(request, 'workout_list.html', {'form': form})

"""



class WorkoutUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Workout
    #form_class = WorkoutModelForm
    fields = ['date','time','workouttype','name','description','feeling','effort','notes','user']
    template_name = 'log/workout_update_form.html'
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'


class WorkoutDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Workout
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'
