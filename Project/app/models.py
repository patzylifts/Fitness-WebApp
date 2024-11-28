from django.db import models

# models for the Goals table
class Goals(models.Model):
    goalID = models.AutoField(primary_key=True)
    goalType =  models.CharField(max_length=100)
    goalDescription = models.TextField()    
    exerciseDuration = models.PositiveIntegerField()

    def __str__(self):
        return self.goalType
    
    

# models for the Client table
class Client(models.Model):
    clientID = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100,null = False) 
    lname = models.CharField(max_length=100, null = False)  
    clientAge=models.PositiveIntegerField()
    clientSex = models.TextChoices('Male', 'Female', 'Other')
    birthdate = models.DateField()
    goal = models.ForeignKey(Goals, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    activityLevel = models.TextChoices('Sedentary', 'Lightly Active', 'Moderately Active', 'Very Active', 'Athlete 2x per day')
    joinedDate = models.DateField(null = False)

    def __str__(self):
        return f"{self.fname} {self.lname} {self.joinedDate}"


# models for the WorkoutPlan table
class WorkoutPlan(models.Model):
    workoutPlanID = models.AutoField(primary_key=True)
    workoutPlanName = models.CharField(max_length=100)
    workoutGoal = models.ManyToManyField(Goals)   
    workoutPlanDescription = models.TextField()
    workoutProgram = models.TextField(max_length=200)

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

    def __str__(self):
        return self.workoutName


# models for the WorkoutLog table
class WorkoutLog(models.Model):
    workoutLogID = models.AutoField(primary_key=True)
    workoutClientName = models.ManyToManyField(Client)
    workoutPlanName = models.ManyToManyField(WorkoutPlan)
    workoutLogGoals = models.ForeignKey(Goals, on_delete= models.CASCADE)
    workoutLogDate = models.DateTimeField()
    workoutPlanDateCreated = models.DateField(null=False)
       
    def __str__(self):
        return str(self.workoutLogDate)
  



