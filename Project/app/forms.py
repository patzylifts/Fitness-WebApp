from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('fname', 'lname', 'clientAge', 'clientSex', 'birthdate', 'goal', 'weight', 'height', 'activityLevel', 'joinedDate')

        widget = {
            'fname': forms.TextInput(attrs={'class': 'form-input',}), 
            'lname': forms.TextInput(attrs={'class': 'form-input'}),
            'clientAge': forms.NumberInput(attrs={'class': 'form-input'}),
            'clientSex': forms.Select(attrs={'class': 'form-select'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-input'}),
            'goal': forms.Select(attrs={'class': 'form-input'}),
            'weight': forms.NumberInput(attrs={'class': 'form-input'}),
            'height': forms.NumberInput(attrs={'class': 'form-input'}),
            'activityLevel': forms.Select(attrs={'class': 'form-select'}),
            'joinedDate': forms.DateInput(attrs={'class': 'form-input'}),

        }