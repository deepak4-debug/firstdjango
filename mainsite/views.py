from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from .models import Carsoul,Car_des,Services,aboutUs,whyUs,list, projects, videos, team

# Create your views here.
def index(request):
    cars = Carsoul.objects.all()
    des = Car_des.objects.all()
    ser = Services.objects.all()
    vid = videos.objects.all()
    index1 = TemplateResponse(request, 'mainsite/index.html', {'cars': cars,'des': des, 'ser':ser,'vid':vid,})
    return index1

    

def contact(request):
    if request.method == "POST":
        Contact_name = request.POST['Contact_name']
        Contact_email = request.POST['Contact_email']
        message = request.POST['message']
        
        # send an mail
        send_mail (
            Contact_name, # Subject
            message, # message
            Contact_email, # from Email
            ['bhattaraid313@gmail.com'], # to email
        )
        
        contact1=TemplateResponse(request, 'mainsite/index.html', {'Contact_name':Contact_name })
        return contact1
        #return render(request, 'contact.html', {'Contact_name':Contact_name })
     
    else:
        contact2=TemplateResponse(request, 'mainsite/index.html', {})
        return contact2
        #return render(request, 'contact.html', {})

     
def service_page1(request):
    service=TemplateResponse(request, 'mainsite/service_page1.html', {})
    return service
    #return render(request, 'service_page1.html', {})

def about_Us(request):
    abu = aboutUs.objects.all()
    whu = whyUs.objects.all()
    lis = list.objects.all()
    context = {
        'abu': abu,
        'whu':whu,
        'lis':lis,
    }
    about = TemplateResponse(request, 'mainsite/aboutUs.html', context)
    return about
    #return render(request, 'aboutUs.html', {})

def ImageGallery(request):
    pro = projects.objects.all()
    context = {
        'pro':pro
    }
    return render(request,'mainsite/img_gallery.html', context)

def Team(request):
    tem = team.objects.all()
    context = {
      'tem':tem  
    }
    return render(request, 'mainsite/team.html', context)