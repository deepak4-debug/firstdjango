# Generated by Django 3.1.5 on 2021-06-26 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_projects_display_project_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_descrption', models.TextField(blank=True, max_length=400)),
                ('Team_Image', models.ImageField(upload_to='team')),
                ('Team_member_name', models.CharField(max_length=30)),
                ('Team_member_designation', models.CharField(max_length=15)),
                ('Team_member_facebook_link', models.URLField(blank=True, db_index=None, unique=True)),
                ('Team_member_google_plus_link', models.URLField(blank=True, db_index=None, unique=True)),
                ('Team_member_twitter_link', models.URLField(blank=True, db_index=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_heading', models.CharField(blank=True, max_length=50)),
                ('Upload_Video', models.FileField(upload_to='videos')),
            ],
        ),
    ]
