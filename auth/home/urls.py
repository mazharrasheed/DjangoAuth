

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index ,name="index"),
    path('login/',views.Log_in ,name="login"),
    path('profile/',views.profile ,name="profile"),
   
]

