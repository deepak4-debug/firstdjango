from django.db import models
from django.db.models.fields import BooleanField, CharField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Carsoul(models.Model):
    height = models.IntegerField(default=954)
    width = models.IntegerField(default=1982)
    Carsoul_image = models.ImageField(upload_to='Cas',height_field='height', width_field='width')
    
    def __str__(self):
        return self.Carsoul_image
    class Meta:
        # Add verbose name
        verbose_name = 'Carsoul Image'

class Car_des(models.Model):
    Car_description = models.TextField(max_length=400)
    
    def __str__(self):
        return self.Car_description
    class Meta:
        # Add verbose name
        verbose_name = 'Carsoul Description'
    
    
class Services(models.Model):
    Services_Image = ImageField(upload_to='ser')
    Services_title = CharField(max_length=40)
    Services_description = TextField()
    
    def __str__(self):
            return self.Services_title
    class Meta:
        # Add verbose name
        verbose_name = 'Service'
    
    
class aboutUs(models.Model):
    AboutUs_description = TextField(max_length=200)
    Sub_header = CharField(max_length=25)
    Sub_Header_description = TextField()
    AboutUs_image = ImageField(upload_to='abu')
    
    def __str__(self):
            return self.Sub_header
    class Meta:
        # Add verbose name
        verbose_name = 'About U'
    
class whyUs(models.Model):
    What_we_do = TextField()
    Why_Choose_us_header = TextField()
    Why_Choose_us_image = ImageField(upload_to='abu')
    
    def __str__(self):
            return self.Why_Choose_us_header
    class Meta:
        # Add verbose name
        verbose_name = 'Why Choose U'
    
class list(models.Model):
    Why_Choose_us_list = TextField(max_length=200)
    
    def __str__(self):
            return self.Why_Choose_us_list
    class Meta:
        # Add verbose name
        verbose_name = 'List of Why choose u'
    
class projects(models.Model):
    Project_Heading = models.TextField(max_length=100, blank=True, null=True)
    Project_Image = ImageField(upload_to='proj')
    PHOTOGRAPHY = 'PHG'
    BRANDING = 'BRN'
    WEB = 'WB'
    
    CATEGORY_OF_PROJECTS_CHOICES = [
        (PHOTOGRAPHY, 'New Projects'),
        (BRANDING, 'Green Building'),
        (WEB, 'Modern Design'),
    ]
    
    category_of_projects = models.CharField(max_length=3, choices=CATEGORY_OF_PROJECTS_CHOICES, default=PHOTOGRAPHY)
    
    def is_upperclass(self):
        return self.category_of_projects in {self.BRANDING, self.WEB}
    
    def __str__(self):
            return self.category_of_projects
    class Meta:
        # Add verbose name
        verbose_name = 'Projects and Image'
    
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
    
    def __str__(self):
            return self.Team_member_name
    class Meta:
        # Add verbose name
        verbose_name = 'Team Members'