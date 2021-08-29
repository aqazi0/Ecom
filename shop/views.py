from typing import ItemsView
from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout
from .models import Product
from math import ceil
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    allprods=[]
    categories=Product.objects.values('category')
    catlist={items['category'] for items in categories}
    for cat in catlist:
        cats=Product.objects.filter(category=cat)
        n=len(cats)
        nslides=n//4+ceil(n/4-(n//4))
        allprods.append([cats, nslides, range(1,nslides)])
    params={'allprods':allprods}    
    return render(request, 'shop/home.html',params)




def about(request):
    return render(request, 'shop/about.html')




def contact(request):
    return render(request, 'shop/contact.html')


def track(request):
    return render(request, 'shop/track.html')

def prodview(request, myid):
    prod=Product.objects.filter(id=myid)
    cat=prod[0].category
    sim_items=Product.objects.filter(category=cat)
    return render(request, 'shop/prodview.html', {'prod':prod, 'items':sim_items})



def catview(request, catid):
    sub_cat={''}
    allprods=[]
    prod=Product.objects.filter(id=catid)
    items=Product.objects.filter(category=prod[0].category)
    for item in items:
        sub_cat.add(item.sub_category)
    sub_cat.remove('')
    for sub in sub_cat:
        sub_category=Product.objects.filter(sub_category=sub)
        n=len(sub_category)
        allprods.append([sub_category, n])
    params={'prods':allprods}
    return render(request, 'shop/catview.html', params)


def checkout(request):
    product=Product.objects.all()
    params={'product':product}
    return render(request, 'shop/checkout.html', params)

def search(request):
    return render(request, 'shop/search.html')


def cart(request):
    return render(request, 'shop/cart.html')


def login(request):
    if(request.method=='POST'):
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        newUser=User.objects.create_user(uname, email, pass1)
        newUser.first_name=fname
        newUser.last_name=lname
        newUser.save()
    return render(request, 'shop/login.html')



def hanlogin(request):
    if request.method=='POST':
        uname=request.POST['loginname']
        password=request.POST['loginpass']
        user=authenticate(username=uname, password=password)
        if user is not None:
            userlogin(request,user)
            return redirect('index')
    return redirect('login')


def logout(request):
    userlogout(request)
    return redirect('index')