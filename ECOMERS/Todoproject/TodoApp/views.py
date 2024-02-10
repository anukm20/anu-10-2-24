from django.shortcuts import render,redirect
import requests
# Create your views here.
def Home(request):
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        return redirect('home')
    return render(request,'index.html',{'data':data})


def Details(req,id):
    data=None
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    
    return render(req,'details.html',{'data':data})


def Category(req,id):
        
    data=None
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    
    return render(req,'category.html',{'data':data})