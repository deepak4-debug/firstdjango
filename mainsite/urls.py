from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.index, name='home'),
    path('services/',views.index, name='services'),
    path('contact/', views.contact, name='contact'),
    path('service_page1', views.service_page1, name='service_page1'),
    path('aboutUs', views.about_Us, name='about_Us'),
    path('image-gallery', views.ImageGallery, name='image-gallery'),
    path('our-team-member', views.Team, name='team')
]
   