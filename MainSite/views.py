

from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

# Create your views here.
def Home(request):
    return render(request,'index.html')


def Contact(request):
    if request.method == "POST":
        msg_name = request.POST['msg_name']
        msg_email = request.POST['msg_email']
        msg_details = request.POST['msg_details']

        ###sending email
        send_mail(
            'Welcome to DentCare',
            'Hello '+ msg_name + 'Your Request: ' + msg_details ,
            'rafialubaba8@gmail.com',
            [ msg_email ]


        )

        return render(request , 'contact.html' , {'name': msg_name })
    
    else:
        return render(request , 'contact.html')


def About(request):
    return render(request,'about.html')

def Appointment(request):
    if request.method == "POST":
        
        app_name= request.POST['app_name']
        app_email= request.POST['app_email']
        app_date= request.POST['app_date']
        app_time= request.POST['app_time']

        context={
          
            'app_name':app_name,
            'app_email':app_email,
            'app_date': app_date,
            'app_time': app_time

        }

        send_mail(

            'DentCare: Apponitment Confirmation',
            'Hello '+ app_name + 'Your  appointment has been fixed.Please review your information. Name: ' + app_name +' Date of Appointment :' + app_date + 'Time: ' + app_time ,
            'rafialubaba8@gmail.com',
            [ app_email ]

        )
        return render(request,'appointment.html' , context)
    else:
        return render(request,'appointment.html')


def Price(request):
    return render(request,'price.html')


def Service(request):
    return render(request,'service.html')


def Team(request):
    team_info = Team_Information.objects.all()
    context={
        'team_info': team_info
    }
    return render(request,'team.html' ,context)