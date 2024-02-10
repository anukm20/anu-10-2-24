from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (req):
    return render(req,'index.html')
def contact (req):
    return render(req,'contact.html')
def des (req):
    return render(req,'destinations.html')
def ele (req):
    return render(req,'elements.html')
def news (req):
    return render(req,'news.html')
