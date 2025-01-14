from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkoutLog, WorkoutPlan, Goals, Client

from .forms import ClientForm, WorkoutLogForm


#Views of the pages
class LoginView(TemplateView):
    template_name = 'apps/login_reg/loginbase.html'

class RegisterView(TemplateView):
    template_name = 'apps/login_reg/register.html'

class HomeView(TemplateView):
    template_name = 'apps/homepages/homepagebase.html'

class HomeFormView(TemplateView):
    template_name = 'apps/homepages/form_popup.html'

class FormInfoView(TemplateView):   
    template_name = 'apps/homepages/form_info.html'

class VideoView(TemplateView):
    template_name = 'apps/homepages/video_popup.html'

# View for WorkoutLog List CRUD
class WorkoutLogListView(ListView):
    model = WorkoutLog
    context_object_name = 'workoutlog_list'
    template_name = 'apps/homepages/workoutlogview.html'
class WorkoutLogDetView(DetailView):
    model = WorkoutLog
    context_object_name = 'workoutlog'
    template_name = 'apps/homepages/workoutlog_detail.html'
class WorkoutLogCreateView(CreateView):
    model = WorkoutLog
    form_class = WorkoutLogForm
    template_name = 'apps/homepages/workoutlog_create.html'
    success_url = reverse_lazy('workoutlog')
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['client_name'] = Client.objects.all()
        context['workout_plan'] = WorkoutPlan.objects.all()      
        context['goal'] = Goals.objects.all() 
        return context
class WorkoutLogUpdateView(UpdateView):
    model = WorkoutLog
    form_class = WorkoutLogForm
    template_name = 'apps/homepages/workoutlog_update.html'
    
    def get_success_url(self):  # Success URL for update
        return reverse_lazy('workoutlog_detail', kwargs={'pk': self.object.pk})
  
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['client_name'] = Client.objects.all()
        context['workout_plan'] = WorkoutPlan.objects.all()      
        context['goal'] = Goals.objects.all() 
        return context
class WorkoutLogDelete(DeleteView):
    model = WorkoutLog
    template_name = 'apps/homepages/workoutlog_delete.html'
    success_url =reverse_lazy('workoutlog')
    
# View for WorkoutPlan View
class WorkoutListView(ListView):
    model = WorkoutPlan
    context_object_name = 'workoutplan_detail'
    template_name = 'apps/homepages/workoutplanview.html'
class ExerciseDetailView(DetailView):
    model = WorkoutPlan
    context_object_name = 'workoutplan'
    template_name = 'apps/homepages/exerciseview.html'

# View for Client Info CRUD
class ClientInfoView(DetailView):
    model = Client
    context_object_name = 'client' 
    template_name = 'apps/homepages/client_infoview.html'
class ClientCreateView(CreateView): 
    model = Client 
    form_class = ClientForm 
    template_name = 'apps/homepages/client_create_edit.html' 
    success_url = reverse_lazy('home') 

    def form_valid(self, form): 
        client = form.save(commit=False) 
        client.bmi = self.calculate_bmi(client.weight, client.height) 
        client.calories = self.calculate_calories(client.weight, client.goal) 
        client.bmi_category = self.bmi_categories(client.bmi) 
        client.save() 
        return super().form_valid(form) 
    def calculate_bmi(self, weight, height): 
        if height == 0: return 0 # To prevent division by zero 
        height_m = height / 100 # Convert cm to meters 
        return round(weight / (height_m * height_m), 2) 
    def calculate_calories(self, weight, goal): 
        maintenance_calories = weight * 24 * 1.2 # Example calculation 
        if goal.name.lower() == 'lose weight': 
            return round(maintenance_calories - 500) 
        elif goal.name.lower() == 'gain weight': 
            return round(maintenance_calories + 500) 
        else: 
            return round(maintenance_calories) 
    def bmi_categories(self, bmi): 
        if bmi < 18.5: 
            return "Underweight" 
        elif bmi >= 18.5 and bmi < 25: 
            return "Normal weight" 
        elif bmi >= 25 and bmi < 30: 
            return "Overweight" 
        else: 
            return "Obese" 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['gender_choices'] = Client.gender_choices 
        context['goal'] = Goals.objects.all() 
        context['activityLevel'] == Client.level_choices 
        return context
class ClientUpdateView(UpdateView): 
    model = Client 
    form_class = ClientForm 
    template_name = 'apps/homepages/client_create_edit.html' 
    success_url = '/home/' 

    def form_valid(self, form): 
        client = form.save(commit=False)
        client.bmi = self.calculate_bmi(client.weight, client.height)
        client.calories = self.calculate_calories(client.weight, client.goal)
        client.bmi_category = self.bmi_categories(client.bmi) 
        client.save() 
        return super().form_valid(form) 
    def calculate_bmi(self, weight, height): 
        if height == 0: 
            return 0 # To prevent division by zero 
        height_m = height / 100 # Convert cm to meters 
        return round(weight / (height_m * height_m), 2) 
    def calculate_calories(self, weight, goal): 
        maintenance_calories = weight * 24 * 1.2 # Example calculation 
        goal_name = str(goal).lower() # Convert goal name to lowercase 
        if goal_name == 'lose weight': 
            return round(maintenance_calories - 500) 
        elif goal_name == 'gain weight': 
            return round(maintenance_calories + 500) 
        else: 
            return round(maintenance_calories)
        
    def bmi_categories(self, bmi): 
        if bmi < 18.5: 
            return "Underweight" 
        elif bmi >= 18.5 and bmi < 25:
            return "Normal weight" 
        elif bmi >= 25 and bmi < 30: 
            return "Overweight" 
        else: 
            return "Obese" 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['gender_choices'] = Client.gender_choices 
        context['goal'] = Goals.objects.all() 
        context['activityLevel'] = Client.level_choices 
        return context