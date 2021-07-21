from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Carsoul(models.Model):
    height = models.IntegerField(default=954)
    width = models.IntegerField(default=1982)
    Carsoul_image = models.ImageField(upload_to='Cas',height_field='height', width_field='width')

class Car_des(models.Model):
    Car_description = models.TextField(max_length=400)
    
class Services(models.Model):
    Services_Image = ImageField(upload_to='ser')
    Services_title = CharField(max_length=40)
    Services_description = TextField()
    
class aboutUs(models.Model):
    AboutUs_description = TextField(max_length=200)
    Sub_header = CharField(max_length=25)
    Sub_Header_description = TextField()
    AboutUs_image = ImageField(upload_to='abu')
    
class whyUs(models.Model):
    What_we_do = TextField()
    Why_Choose_us_header = TextField()
    Why_Choose_us_image = ImageField(upload_to='abu')
    
class list(models.Model):
    Why_Choose_us_list = TextField(max_length=200)
    
    
class projects(models.Model):
    Project_Heading = models.TextField(max_length=100, blank=True, null=True)
    Project_Image = ImageField(upload_to='proj')
    PHOTOGRAPHY = 'PHG'
    BRANDING = 'BRN'
    WEB = 'WB'
    
    CATEGORY_OF_PROJECTS_CHOICES = [
        (PHOTOGRAPHY, 'Photography'),
        (BRANDING, 'Branding'),
        (WEB, 'Web'),
    ]
    
    category_of_projects = models.CharField(max_length=3, choices=CATEGORY_OF_PROJECTS_CHOICES, default=PHOTOGRAPHY)
    
    def is_upperclass(self):
        return self.category_of_projects in {self.BRANDING, self.WEB}
    
    
class videos(models.Model):
    Display_Video_heading = models.BooleanField(default=False)
    Video_heading = models.CharField(max_length=50, blank=True, null=True)
    Upload_Video = models.FileField(upload_to='videos')
    
class team(models.Model):
    Team_descrption = models.TextField(max_length=400, blank=True, null=True)
    Team_Image = models.ImageField(upload_to='team')
    Team_member_name = models.CharField(max_length=30)
    Team_member_designation = models.CharField(max_length=15)
    Team_member_facebook_link = models.URLField(max_length=200, db_index=None, unique=True, blank=True, null=True)
    Team_member_google_plus_link = models.URLField(max_length=200, db_index=None, unique=True, blank=True, null=True)
    Team_member_twitter_link = models.URLField(max_length=200, db_index=None, unique=True, blank=True, null=True)
    