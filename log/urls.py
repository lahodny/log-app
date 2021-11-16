from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workouts/', views.WorkoutListView.as_view(), name='workouts'),
    path('workout/<int:pk>', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('workout/<int:pk>/update/', views.WorkoutUpdateView.as_view(), name='workout-update'),
    path('workout/<int:pk>/delete/', views.WorkoutDeleteView.as_view(), name='workout-delete'),
    path('workout/create/', views.WorkoutCreateView.as_view(), name='workout-create'),
]