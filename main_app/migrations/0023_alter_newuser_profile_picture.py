# Generated by Django 4.2.16 on 2024-09-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_alter_newuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]