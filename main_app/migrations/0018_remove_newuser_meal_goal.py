# Generated by Django 4.2.16 on 2024-09-20 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_newuser_meal_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='meal_goal',
        ),
    ]