from django.shortcuts import render,redirect
import requests
# Create your views here.
def Home(request):
    data=None
    cat=None
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()   
        cat=list(set(product['category'] for product in data['products']))
        print(data)
    return render(request,'index.html',{'cat':cat,'data':data})


def Details(req,id):
    data=None
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    
    return render(req,'details.html',{'data':data})


def Smart(req,cat):
    a=[]
    print(cat)
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        for i in data['products']:
            if cat in i['category']:
                a.append(i)
        print(a)
    return render(req,'smart.html',{'data':a})

def addcart(req,id):
    data=None
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        cart=cart(price=data['id'],product_name=data['title'],brand=data['brand'],image=data['thummnail'])
        cart.save()
    return redirect('cart')

def cart(req):
    cart=cart.objects.all()
    return render(req,'cart.html',{'cart':cart})


def delete(req,id):
    cart.objects.filter(id=id).delete()
    return redirect('cart')