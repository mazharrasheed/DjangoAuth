from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login
from django.contrib import messages
from .forms import SignUp

# Create your views here.

def index(request):

    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created succesfuly !!")

    else:
        form=SignUp()

    data={'form':form,'signin':True}
    return render(request,"index.html",data)

def Log_in(request):
    mydata={}
    if request.method=='POST':
        login_form=AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            uname=login_form.cleaned_data['username']
            upass=login_form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,"You are successfuly loged_in")
                return HttpResponseRedirect("/profile/")
    else:
        login_form=AuthenticationForm()
    mydata={'form':login_form}
    return render(request,"index.html",mydata)

def profile(request):
    return render(request,"profile.html")
