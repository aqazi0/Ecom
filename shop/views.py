from typing import ItemsView
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout
from .models import Product, categorie, address, UserProfile
from math import ceil
from django.contrib.auth.models import User
from itertools import chain
# Create your views here.


def index(request):
    totalcat=categorie.objects.all()
    allprods=[]
    categories=Product.objects.values('category')
    catlist={items['category'] for items in categories}
    for cat in catlist:
        cats=Product.objects.filter(category=cat)
        n=len(cats)
        nslides=n//4+ceil(n/4-(n//4))
        allprods.append([cats, nslides, range(1,nslides)])
    if request.user.is_authenticated:
        if len(UserProfile.objects.filter(user=request.user)) != 0:
            cart=UserProfile.objects.filter(user=request.user)[0].cartjson
        else:    
            addr=address(user=request.user, name=request.user.first_name, email=request.user.email, phone='000000', add='', city='', state='', pin=123456)
            addr.save()
            userdata=UserProfile(user=request.user, cartjson='{}', address=addr)
            userdata.save()
            cart='{}'
        params={'allprods':allprods, 'categories':totalcat, "catrange":range(1,1), 'cart':cart}
    else:
        params={'allprods':allprods, 'categories':totalcat, "catrange":range(1,1)}
    return render(request, 'shop/home.html',params)


def prodview(request, myid):
    prod=Product.objects.filter(id=myid)
    cat=prod[0].category
    sim_items=Product.objects.filter(category=cat)
    if request.user.is_authenticated:
        if len(UserProfile.objects.filter(user=request.user)) != 0:
            cart=UserProfile.objects.filter(user=request.user)[0].cartjson
        else:
            cart='{}'
        params={'prod':prod, 'items':sim_items, 'cart':cart}
    else:
        params={'prod':prod, 'items':sim_items}
    return render(request, 'shop/prodview.html', params)


def catview(request, catid):
    sub_cat={''}
    allprods=[]
    cat=categorie.objects.filter(id=catid)[0].category
    items=Product.objects.filter(category=cat)
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
    if request.method=='POST':
        cart=request.POST['cartjson']
        name=request.POST['fullname']
        mail=request.POST['email']
        tel=request.POST['phone']
        add=request.POST['add']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        print(cart, type(cart))
        addr=address(user=request.user, name=name, email=mail, phone=tel, add=add, city=city, state=state, pin=zip)
        addr.save()
        Userdetail=UserProfile(user=request.user,cartjson=cart, address=addr)
        Userdetail.save()
    return render(request, 'shop/checkout.html', params)


def cart(request):
    params={}
    if request.user.is_authenticated:
        cart=UserProfile.objects.filter(user=request.user)[0].cartjson
        if request.method=='POST':
            userdata=UserProfile.objects.get(user=request.user)
            cart=request.POST['cartjson']
            userdata.cartjson=cart
            userdata.save()
            params={'cart':cart}
    return render(request, 'shop/cart.html',params)


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
    if request.user.is_authenticated:
        return redirect('index')
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


def search(request):
    query=request.GET['query']
    if(len(query)==0 or len(query) > 80):
        prods=Product.objects.none()
    else:
        name=Product.objects.filter(product_name__contains=query)
        cat=Product.objects.filter(category__contains=query)
        subcat=Product.objects.filter(sub_category__contains=query)
        desc=Product.objects.filter(desc__contains=query)
        prods=((name.union(cat)).union(subcat)).union(desc)
    params={'allprods':prods, 'query':query}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def track(request):
    return render(request, 'shop/track.html')