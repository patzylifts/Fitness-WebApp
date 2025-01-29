from django import forms
from .models import Client, WorkoutLog

from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['fname', 'lname', 'clientAge', 'clientSex', 'birthdate', 'weight', 'height', 'activityLevel']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'clientAge': forms.NumberInput(attrs={'class': 'form-control'}),
            'clientSex': forms.Select(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'activityLevel': forms.Select(attrs={'class': 'form-control'}),
        }

class WorkoutLogForm(forms.ModelForm): 
    class Meta: 
        model = WorkoutLog 
        fields = ['workoutClientName', 'workoutPlanName', 'workoutLogGoals', 'workoutLogDate']