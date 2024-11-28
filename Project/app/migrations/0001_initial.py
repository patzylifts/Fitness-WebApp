# Generated by Django 5.1.2 on 2024-11-13 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('goalID', models.AutoField(primary_key=True, serialize=False)),
                ('goalType', models.CharField(max_length=100)),
                ('goalDescription', models.TextField()),
                ('exerciseDuration', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exerciseID', models.AutoField(primary_key=True, serialize=False)),
                ('workoutName', models.CharField(max_length=100)),
                ('workoutType', models.CharField(max_length=100)),
                ('workoutDescription', models.TextField()),
                ('workoutSets', models.CharField(max_length=20)),
                ('workoutReps', models.CharField(max_length=20)),
                ('goalType', models.ManyToManyField(to='app.goals')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('clientID', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('clientAge', models.PositiveIntegerField()),
                ('birthdate', models.DateField()),
                ('weight', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('joinedDate', models.DateField()),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.goals')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('workoutPlanID', models.AutoField(primary_key=True, serialize=False)),
                ('workoutPlanName', models.CharField(max_length=100)),
                ('workoutPlanType', models.CharField(max_length=100)),
                ('workoutPlanDescription', models.TextField()),
                ('workoutDuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('workoutLogID', models.AutoField(primary_key=True, serialize=False)),
                ('workoutLogDate', models.DateTimeField()),
                ('workoutPlanDateCreated', models.DateField()),
                ('workoutClientName', models.ManyToManyField(to='app.client')),
                ('workoutLogGoals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.goals')),
                ('workoutPlanName', models.ManyToManyField(to='app.workoutplan')),
            ],
        ),
    ]
