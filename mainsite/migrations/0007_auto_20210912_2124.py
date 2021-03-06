# Generated by Django 3.2.6 on 2021-09-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_videos_display_video_heading'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About U'},
        ),
        migrations.AlterModelOptions(
            name='car_des',
            options={'verbose_name': 'Carsoul Description'},
        ),
        migrations.AlterModelOptions(
            name='carsoul',
            options={'verbose_name': 'Carsoul Image'},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'List of Why choose u'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Projects and Image'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team Members'},
        ),
        migrations.AlterModelOptions(
            name='whyus',
            options={'verbose_name': 'Why Choose U'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='category_of_projects',
            field=models.CharField(choices=[('PHG', 'New Projects'), ('BRN', 'Green Building'), ('WB', 'Modern Design')], default='PHG', max_length=3),
        ),
    ]
