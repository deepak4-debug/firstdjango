from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.index, name='home'),
    path('services/',views.index, name='services'),
    path('aboutUs/',views.index, name='aboutUs'),
    path('projects/',views.index, name='projects'),
    path('team/',views.index, name='team'),
    path('contact/', views.contact, name='contact'),
    path('service_page1', views.service_page1, name='service_page1'),
    path('aboutUs', views.about_Us, name='about_Us'),
]
   