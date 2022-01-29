
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import Contact,About,Appointment,Price,Service,Home,Team

urlpatterns = [
    path('' , views.Home , name="home"),
    path('contact' , views.Contact , name="contact"),
    path('about',views.About,name="about"),
    path('appointment',views.Appointment,name="appointment"),
    path('price',views.Price,name="price"),
    path('service',views.Service,name="service"),
    path('team',views.Team,name="team")
]
