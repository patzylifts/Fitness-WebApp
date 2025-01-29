from django.shortcuts import render,redirect,  get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkoutLog, WorkoutPlan, Goals, Client, Exercise

from .forms import ClientForm, WorkoutLogForm


#Views of the pages

from django.shortcuts import render
from .models import Client

def some_view(request):
    client = None
    if request.user.is_authenticated:
        client = Client.objects.filter(user=request.user).first()
    return render(request, 'your_template.html', {'client': client})

class HomeView(TemplateView): 
    template_name = 'apps/homepages/homepagebase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()  # Pass clients to the template
        return context

class HomeFormView(TemplateView):
    template_name = 'apps/homepages/form_popup.html'

class FormInfoView(TemplateView):   
    template_name = 'apps/homepages/form_info.html'

class VideoView(TemplateView):
    template_name = 'apps/homepages/video_popup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.all()  # Pass exercises to the template
        return context

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


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add 'clients' to the context
        context['clients'] = Client.objects.all()  # Filter as necessary
        return context
from django.views.generic import DetailView
from .models import WorkoutPlan, Exercise

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

class ExerciseDetailView(DetailView):
    model = WorkoutPlan
    context_object_name = 'workoutplan'
    template_name = 'apps/homepages/exerciseview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the current workout plan object
        workout_plan = self.get_object()

        # Count the number of exercises related to this workout plan
        total_exercises = Exercise.objects.filter(workoutType=workout_plan).count()

        # Calculate the total sets for all exercises in this workout plan
        total_sets = 0
        for exercise in workout_plan.exercise_set.all():
            try:
                sets = exercise.workoutSets.split('x')[0]  # Extract the number of sets
                total_sets += int(sets)
            except ValueError:
                continue

        # Get the search query
        query = self.request.GET.get('q', '')

        # Filter exercises based on the search query
        if query:
            filtered_exer = Exercise.objects.filter(workoutName__icontains=query, workoutType=workout_plan)
        else:
            filtered_exer = Exercise.objects.filter(workoutType=workout_plan)

        context['workoutplan'] = workout_plan
        context['filtered_exer'] = filtered_exer  # Use the filtered exercises
        context['total_program'] = total_exercises
        context['total_sets'] = total_sets

        return context

# View for Client Info CRUD

class ClientInfoView(DetailView):
    model = Client
    context_object_name = 'client'
    template_name = 'apps/homepages/client_infoview.html'

class ClientInfosView(ListView):
    model = Client
    context_object_name = 'clients'

from django.shortcuts import get_object_or_404, redirect
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
        form.instance.user = self.request.user
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
        context['activityLevel'] = context.get('activityLevel', Client.level_choices)
        return context
class ClientUpdateView(UpdateView): 
    model = Client 
    form_class = ClientForm 
    template_name = 'apps/homepages/client_create_edit.html' 
   
    def get_success_url(self):
        return reverse('client_info', kwargs={'pk': self.object.pk})

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