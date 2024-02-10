from django.shortcuts import render
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def Signup(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        email=req.POST.get('email','')
    return render(req,'signup.html')
        