# Generated by Django 5.1.2 on 2024-12-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_client_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='activityLevel',
            field=models.CharField(choices=[('Sedentary', 'Sedentary'), ('Lightly Active', 'Lightly Active'), ('Moderately Active', 'Moderately Active'), ('Very Active', 'Very Active'), ('Athlete 2x per day', 'Athlete 2x per day')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='clientSex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('', 'Other')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
