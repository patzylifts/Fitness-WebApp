# Generated by Django 5.1.2 on 2024-12-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_client_bmi_client_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='bmi_category',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
