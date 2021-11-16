from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from log.models import Workout, WorkoutType


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


class WorkoutListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Workout
    context_object_name = 'workouts_list'
    permission_required = 'log.see_list'

    def get_queryset(self):
            return Workout.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkoutDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Workout
    permission_required = 'log.see_detail'


class WorkoutCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Workout
    fields = ['date','time','workouttype','name','description','feeling','effort','notes']
    success_url = reverse_lazy('workouts')
    #login_url = '/accounts/login/'
    permission_required = 'log.add_workout'


class WorkoutUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Workout
    #form_class = WorkoutModelForm
    fields = ['date','time','workouttype','name','description','feeling','effort','notes']
    template_name = 'log/workout_update_form.html'
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'
    permission_required = 'log.change_workout'


class WorkoutDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Workout
    success_url = reverse_lazy('workouts')
    login_url = '/accounts/login/'
    permission_required = 'log.delete_workout'
