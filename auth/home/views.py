from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from django.contrib import messages
from .forms import SignUp

# Create your views here.

def index(request):

    if request.method=='POST':
       pass
    else:
        pass

    data={}
    return render(request,"index.html",data)

def sign_up(request):

    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created succesfuly !!")

    else:
        form=SignUp()

    data={'form':form}
    return render(request,"signup.html",data)

def Log_in(request):
    mydata={}
    if not request.user.is_authenticated:
        if request.method=='POST':
            login_form=AuthenticationForm(request=request,data=request.POST)
            if login_form.is_valid():
                uname=login_form.cleaned_data['username']
                upass=login_form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"You are successfuly login")
                    return HttpResponseRedirect("/profile/")
        else:
            login_form=AuthenticationForm()
        mydata={'form':login_form}
        return render(request,"signin.html",mydata)
    else:return redirect("profile")

def profile(request):
    if request.user.is_authenticated:
        name=request.user
        data={'name':name}
        print(name)
        return render(request,"profile.html",data)
    else:
        return redirect("login")
    
def log_out(request):

    logout(request)
    return redirect("login")

def change_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request,"Password Changed Succesfully")
                return redirect("profile")
        else:
            form=PasswordChangeForm(user=request.user)
        data1={'form':form}
        return render(request,'changepass.html',data1)
    else:
        return redirect("login")
    
def set_pass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request,"Password Changed Succesfully")
                return redirect("profile")
        else:
            form=SetPasswordForm(user=request.user)
        data1={'form':form}
        return render(request,'changepass1.html',data1)
    else:
        return redirect("login")
