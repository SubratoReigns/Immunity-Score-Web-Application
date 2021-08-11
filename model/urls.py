
from django.contrib import admin
from django.urls import path
from model import views

urlpatterns = [
    path("", views.modelhome, name = 'modelhome'),
    path("diabetes", views.ddisease, name = 'diabetes'),
    path("diabetesf", views.dform, name = 'diabetesf'),
    path("result", views.result2, name = 'result2'),  
] 
