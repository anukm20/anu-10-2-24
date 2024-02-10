from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .models import College



def Home(req):
    colleges=College.objects.all()
    return render(req,'index.html',{'colleges':colleges})
from django.shortcuts import render,redirect

def registerUser(req):
    if req.method=="POST":
        fname=req.POST.get("fname","")
        lname=req.POST.get("lname","")
        email=req.POST.get("email","")
        username=req.POST.get("username","")
        password=req.POST.get("password","")
        cpassword=req.POST.get("cpassword","")
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(req,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                return redirect('loginuser')
        else:
            messages.info(req,"password not matched")
            return redirect('home')
    
    return render(req,'registeruser.html')



