from django.contrib import admin
from django.urls import path
from newapp import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('flavours',views.flavours,name="flavours"),
    path('contact',views.contact,name="contact"),
    path('hello world',views.helloworld,name="hello world"),
    path('connect with us',views.connectwithus,name="connect with us"),

]