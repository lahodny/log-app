from django.urls import path
from . import views

app_name = 'log'
urlpatterns = [
    path('', views.index, name='index'),
    path('workouts/', views.WorkoutListView.as_view(), name='workouts'),
    path('workout/<int:pk>', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('workout/<int:pk>/update/', views.WorkoutUpdateView.as_view(), name='workout-update'),
    path('workout/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='workout-delete'),
    path('workout/create/', views.create, name='workout-create'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('workout/<workout_id>/edit/', views.workout, name='workout_edit'),
    path('workout/new/<workout_date>/', views.workoutdate, name='workout_date'),
    path('workouts/search/', views.workoutsearch, name='workout-search'),
    path('profile/', views.type, name='type'),
]
