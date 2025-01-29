from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# models for the Goals table
class Goals(models.Model):
    goalID = models.AutoField(primary_key=True)
    goal =  models.CharField(max_length=100)
    
    goalDescription = models.TextField()    
    exerciseDuration = models.PositiveIntegerField()

    def __str__(self):
        return self.goal

# models for the Client table
class Client(models.Model):  
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    clientID = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100,null = False) 
    lname = models.CharField(max_length=100, null = False)  
    clientAge=models.PositiveIntegerField()
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('', 'Other'),
    )
    clientSex = models.CharField(max_length=10, choices=gender_choices)
    birthdate = models.DateField()
    goal = models.ForeignKey(Goals, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    level_choices = (
        ('Sedentary', 'Sedentary'),
        ('Lightly Active', 'Lightly Active'),
        ('Moderately Active', 'Moderately Active'),
        ('Very Active', 'Very Active'),
        ('Athlete 2x per day', 'Athlete 2x per day'),
    )
    activityLevel = models.CharField(max_length=100, choices=level_choices)
    joinedDate = models.DateField(null = False)
    bmi = models.FloatField(null=True, blank=True) 
    calories = models.FloatField(null=True, blank=True)
    bmi_category = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname} {self.joinedDate}"


# models for the WorkoutPlan table
class WorkoutPlan(models.Model):
    workoutPlanID = models.AutoField(primary_key=True)
    workoutPlanName = models.CharField(max_length=100)
    workoutGoal = models.ManyToManyField(Goals)   
    workoutPlanDescription = models.TextField()
    workoutProgram = models.TextField(max_length=1200)

    def __str__(self):
        return self.workoutPlanName

# models for the Workout table
class Exercise(models.Model):
    exerciseID = models.AutoField(primary_key=True)
    workoutName = models.CharField(max_length=100)
    workoutType = models.ManyToManyField(WorkoutPlan)
    workoutDescription = models.TextField() 
    workoutSets = models.CharField(max_length=20)
    workoutReps = models.CharField(max_length=20)
    workoutLink = models.URLField() 
    
    def __str__(self):
        return self.workoutName


# models for the WorkoutLog table
class WorkoutLog(models.Model):
    workoutLogID = models.AutoField(primary_key=True)
    workoutClientName = models.ManyToManyField(Client)
    workoutPlanName = models.ManyToManyField(WorkoutPlan)
    workoutLogGoals = models.ForeignKey(Goals, on_delete= models.CASCADE)
    workoutLogDate = models.DateTimeField(null=False)
    workoutPlanDateCreated = models.DateField()
       
    def __str__(self):
        return str(self.workoutLogDate)
  



