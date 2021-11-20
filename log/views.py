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
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from .forms import Calendar
import calendar
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect



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


class WorkoutUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Workout
    #form_class = WorkoutModelForm
    fields = ['date','time','workouttype','name','description','feeling','effort','notes']
    template_name = 'log/workout_update_form.html'
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'


class WorkoutDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Workout
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Workout
    template_name = 'log/calendar.html'

    def get_context_data(self, just=None, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))
        just = self.request.user
        cal = Calendar(d.year, d.month, just)
        html_cal = cal.formatmonth(withyear=True)

        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def workout(request, workout_id=None):
    instance = Workout()
    if workout_id:
        instance = get_object_or_404(Workout, pk=workout_id)
    else:
        instance = Workout()
    form = WorkoutForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return HttpResponseRedirect('/log/calendar/')
        else:
            form = WorkoutForm

    return render(request, 'log/workout_form.html', {'form': form})


