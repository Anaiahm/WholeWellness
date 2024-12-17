# Generated by Django 4.2.16 on 2024-09-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_newuser_meal_goal_alter_meal_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snack')], default='B', max_length=50, verbose_name='Select Meal'),
        ),
    ]