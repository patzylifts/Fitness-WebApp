# Generated by Django 5.1.2 on 2025-01-25 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_exercise_workoutlink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goals',
            old_name='goal_name',
            new_name='name',
        ),
    ]
