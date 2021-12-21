from django.contrib import admin



from .models import *

# Registrace modelů v administraci aplikace

admin.site.register(Workout)
admin.site.register(WorkoutType)
admin.site.register(Discipline)
admin.site.register(Performances)


#@admin.register(Workout)
#class WorkoutAdmin(admin.ModelAdmin):
#    list_display =  fields = ('date','time','workouttype','name','description','feeling','effort','notes','user')
