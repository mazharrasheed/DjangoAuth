

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [

    path('',views.index ,name="index"),
    path('signup/',views.sign_up ,name="signup"),
    path('login/',views.Log_in ,name="login"),
    path('profile/',views.profile ,name="profile"),
    path('editprofile/',views.editprofile ,name="editprofile"),
    path('logout/',views.log_out ,name="logout"),
    path('changepass/',views.change_pass ,name="changepass"),
    path('changepass1/',views.set_pass ,name="changepass1"),
    path('userdetail/<int:id>',views.user_detail ,name="userdetail"),
   
]

