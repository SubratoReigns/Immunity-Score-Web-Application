
from django.contrib import admin
from django.urls import path
from blog import views
from . import views

urlpatterns = [
    
    # APIs to post a comment
    path('postComment', views.postComment, name = 'postComment'), 
    path("", views.blogh, name = 'bloghome'),
    path('<str:slug>', views.blogp, name = 'blogpost'),
 
] 
