from django.contrib import admin



from .models import *

# Registrace modelů v administraci aplikace

admin.site.register(Workout)
admin.site.register(WorkoutType)