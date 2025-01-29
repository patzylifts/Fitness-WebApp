from django.urls import path
from .views import  HomeView, FormInfoView, VideoView, WorkoutLogListView, WorkoutLogDetView, WorkoutLogCreateView,  WorkoutLogUpdateView, WorkoutLogDelete, WorkoutListView, ExerciseDetailView, ClientInfoView,ClientCreateView, ClientUpdateView
from . import views
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('info/form', FormInfoView.as_view(), name='form_info'),
    path('video-popup/', VideoView.as_view(), name='video_popup'),
    
    #details of the workoutplan view
    path('workoutplans/', WorkoutListView.as_view(), name='workoutplan_list'),   
    path('workoutplans/<int:pk>/', ExerciseDetailView.as_view(), name='workoutplan_detail'),
    path('exercises/', views.exercise_list, name='exercise_list'),


    #details of the workoutlog CRUD
    path('home/workoutlog/', WorkoutLogListView.as_view(), name= 'workoutlog'),
    path('home/workoutlog/<int:pk>/', WorkoutLogDetView.as_view(), name='workoutlog_detail'),
    path('home/workoutlog/create/', WorkoutLogCreateView.as_view(), name='workoutlog_create'),
    path('home/workoutlog/edit/<int:pk>/', WorkoutLogUpdateView.as_view(), name='workoutlog_update'),
    path('home/workoutlog/delete/<int:pk>/', WorkoutLogDelete.as_view(), name='workoutlog_delete'),

    #details of the client CRUD
    path('info/<int:pk>/', ClientInfoView.as_view(), name='client_info'),
    path('info/create/', ClientCreateView.as_view(), name= 'client_profile'),
    path('info/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
       
    ]

