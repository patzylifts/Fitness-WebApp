from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import WorkoutLog, WorkoutPlan, Goals, Client
from django.contrib.auth.models import User
from .forms import ClientForm


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


# View for WorkoutLog List
class WorkoutLogListView(ListView):
    model = WorkoutLog
    context_object_name = 'workoutlog_list'
    template_name = 'apps/homepages/workoutlogview.html'
  
# View for WorkoutPlan View
class WorkoutListView(ListView):
    model = WorkoutPlan
    context_object_name = 'workoutplan_detail'
    template_name = 'apps/homepages/workoutplanview.html'
class ExerciseDetailView(DetailView):
    model = WorkoutPlan
    context_object_name = 'workoutplan'
    template_name = 'apps/homepages/exerciseview.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    # fields = ['fname', 'lname', 'clientAge', 'clientSex', 'birthdate', 'goal','weight', 'height', 'activityLevel', 'joinedDate']
    #context_object_name = 'client'

    template_name = 'apps/homepages/clientview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        context['gender_choices'] = Client.gender_choices
        context['goal'] = Goals.objects.all()
        context['activityLevel'] = Client.level_choices
       
        return context     


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'apps/homepages/clientview.html'