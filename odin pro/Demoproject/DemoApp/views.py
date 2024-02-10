from django.shortcuts import render
from django.http import HttpResponse

def Home(req):
    return render(req,'index.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')