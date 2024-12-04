from django.urls import path
from .views import LoginView, RegisterView, HomeView, FormInfoView, WorkoutLogListView, WorkoutDetailView, ClientCreateView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('reg/', RegisterView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
   # path('info/form', FormInfoView.as_view(), name='form_info'),
    path('home/workoutlog/', WorkoutLogListView.as_view(), name= 'workoutlog'),
    path('home/workoutdetail/<int:pk>', WorkoutDetailView.as_view(), name= 'workoutplan'),   
    path('info/create/',ClientCreateView.as_view(), name= 'client_profile'),
       
    ]

