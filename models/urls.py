
from django.contrib import admin
from django.urls import path
from models import views


urlpatterns = [
    path("", views.modelhome, name = 'modelhome'),
    path("diabetes", views.ddisease, name = 'diabetes'),
    path("heartf", views.hform, name = 'heartf'),
    path("diabetesf", views.dform, name = 'diabetesf'),
    path("result", views.result2, name = 'result2'),
    path("result1", views.result3, name = 'result3'),
    path("heartf1", views.hform1, name = 'heartf1'),
    path("resultn1", views.result4, name = 'result_4'),
    ] 
