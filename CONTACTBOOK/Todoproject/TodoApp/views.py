from django.shortcuts import render,redirect
from .models import Contact


def Home(req):
    contacts=Contact.objects.all()
    return render(req,'index.html',{'contacts':contacts})

def Newcontact(req):
    if req.method=="POST": 
        image=req.FILES['image'] 
        name=req.POST.get('name','')
        phone=req.POST.get('phone','')
        email=req.POST.get('email','')
        address=req.POST.get('address','')      
        contact=Contact(image=image,name=name,phone=phone,email=email,address=address)
        contact.save()
        return redirect('home')
    return render(req,'newcontact.html')