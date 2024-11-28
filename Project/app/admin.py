from django.contrib import admin
from .models import  Exercise, Goals, Client, WorkoutPlan, WorkoutLog

# Register your models here.

admin.site.register(Client)
admin.site.register(Goals)
admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutLog)

