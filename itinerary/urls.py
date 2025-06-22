from django.contrib import admin
from django.urls import path 
from itinerary import views

urlpatterns = [    
    path('',views.home, name="home"),
    path('Destinations/',views.Destinations, name="Destinations"),
    path('about/',views.about, name="about"),
    path('contacts/',views.contacts, name="contact"),
    path('login/',views.login, name="login"),
    path('register/',views.register, name="register"),
    path('detail/',views.detail, name="detail"),
    path('planTrip/',views.planTrip, name="planTrip"),
    path('detail/', views.detail, name="detail"),
    

]
