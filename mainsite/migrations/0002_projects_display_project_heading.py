# Generated by Django 3.1.5 on 2021-06-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Display_Project_heading',
            field=models.BooleanField(default=False),
        ),
    ]