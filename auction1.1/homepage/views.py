from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Item,Painting,Antique,Cart
from .models import Myuser,User
import random
import datetime
from .forms import uform
from django.http import JsonResponse
from django import forms

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse


def index(request):
    return render(request, 'homepage/index.html')


def item(request):
    items=Item.objects.all()
    return render(request, 'homepage/item.html',{'items':items})


def antique(request):
    antiques=Antique.objects.all()
    return render(request, 'homepage/antique.html', {'antiques':antiques})


def painting(request):
    paintings=Painting.objects.all()
    return render(request, 'homepage/painting.html',{'paintings':paintings})


def getreg(request):
    form=uform()
    return render(request,'homepage/register.html',{'form':form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('homepage:index')
            else:
                return render(request, 'homepage/register.html')
        else:
            return render(request, 'homepage/register.html')
    return render(request, 'homepage/register.html')


def detailview(request, pk):
    top=0
    cup=0
    cover = 0
    f=0
    today_date = datetime.date.today()
    pk1 = int(pk)
    if pk1 < 100:
        top = Item.objects.get(item_id=pk)
        end_date = top.item_enddate
    elif pk1 <200:
        cup = Painting.objects.get(painting_id=pk)
        end_date = cup.painting_enddate
    elif pk1<300:
        cover = Antique.objects.get(antique_id=pk)
        end_date = cover.antique_enddate
    year = end_date.year
    month = end_date.month
    date = end_date.day
    if today_date<end_date:
        f=0
    else:
        f=1
    context = {'pk': pk, 'cup': cup, 'top': top, 'cover': cover,'end_date':end_date,'month':month,'date':date,'year':year,'f':f}
    return render(request, 'homepage/detail.html', context)


def regi(request):
    if request.method=='POST':
        form = uform(request.POST,request.FILES)
        existing = User.objects.filter(username__iexact=request.POST.get('username',''))
        if existing.exists():
            return HttpResponse("A user with that username already exists.")
        eml = request.POST.get('email', '')
        if "@" not in eml:
            return HttpResponse("Please enter an Email Address with a valid domain")
        domain = eml.split('@')[1]
        domain_list = ["gmail.com", "yahoo.com", "hotmail.com","rediff.com","gmail.in", "yahoo.in", "hotmail.co.in","rediff.co.in"]
        if domain not in domain_list:
            return HttpResponse("Please enter an Email Address with a valid domain")
        if form.is_valid():
            user = form.save(commit=False)
            first_name = request.POST.get('first_name', '')
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            cpassword = request.POST.get('cpassword', '')
            if password!=cpassword:
                return HttpResponse("Passwords don't match")
            else:
                password = request.POST.get('password', '')
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    ob = Myuser()
                    ob.user1 = request.user
                    ob.save()
                    return redirect('homepage:index')
                else:
                    return redirect('homepage:register')
            else:
                return redirect('homepage:register')
        else:
            return redirect('homepage:register')


def logout_user(request):
    logout(request)
    return redirect('homepage:index')


def bid(request, pk):
    pk1 = int(pk)
    if pk1 < 100:
        top = Item.objects.get(item_id=pk)
        z = top.item_bidprice
        z = z + 5000
        Item.objects.filter(item_id=pk).update(item_bidprice=z)
        Item.objects.filter(item_id=pk).update(item_owner=request.user)
    elif pk1 < 200:
        cup = Painting.objects.get(painting_id=pk)
        z = cup.painting_bidprice
        z = z + 5000
        Painting.objects.filter(painting_id=pk).update(painting_bidprice=z)
        Painting.objects.filter(painting_id=pk).update(painting_owner=request.user)
    elif pk1 < 300:
        cover = Antique.objects.get(antique_id=pk)
        z = cover.antique_bidprice
        z = z + 5000
        Antique.objects.filter(antique_id=pk).update(antique_bidprice=z)
        Antique.objects.filter(antique_id=pk).update(antique_owner=request.user)
    return redirect('homepage:detail', pk)


def team(request):
    return render(request, 'homepage/team.html')


def cart(request):
    if request.user.is_authenticated():
        obj=Cart.objects.filter(user=request.user)
        return render(request, 'homepage/cart.html', {'obj': obj})
    else:
        return redirect('homepage:register')


def checkout(request):
    if request.user.is_authenticated():
        return redirect('homepage:checkout')
    else:
        redirect('homepage:register')


def cart1(request, pk):
    if not request.user.is_authenticated():
        return redirect('homepage:register')
    else:
        pk1 = int(pk)
        if pk1 < 100:
            top = Item.objects.get(item_id=pk)
            ob = Cart()
            ob.user = top.item_owner
            ob.price = top.item_bidprice
            ob.title = top.item_title
            ob.pic = top.item_pic
            ob.auc_id1 = Item.objects.get(item_id=pk)
            ob.save()
            z = top.item_price
            Item.objects.filter(item_id=pk).update(item_bidprice=z)
        elif pk1 < 200:
            cup = Painting.objects.get(painting_id=pk)
            ob = Cart()
            ob.user = cup.painting_owner
            ob.price = cup.painting_bidprice
            ob.title = cup.painting_title
            ob.pic = cup.painting_pic
            ob.auc_id2 = Painting.objects.get(painting_id=pk)
            ob.save()
            z = cup.painting_price
            Painting.objects.filter(painting_id=pk).update(painting_bidprice=z)
        elif pk1 < 300:
            cover = Antique.objects.get(antique_id=pk)
            ob = Cart()
            ob.user = cover.antique_owner
            ob.price = cover.antique_bidprice
            ob.title = cover.antique_title
            ob.pic = cover.antique_pic
            ob.auc_id3 = Antique.objects.get(antique_id=pk)
            ob.save()
            z = cover.antique_price
            Antique.objects.filter(antique_id=pk).update(antique_bidprice=z)
        return redirect('homepage:index')

def final(request):
    y = 0
    now = datetime.datetime.now()
    d = str(now)
    cart = Cart.objects.filter(user=request.user)
    for t in cart:
        y = y + int(t.price)
    if request.method=='POST':
        u = Myuser.objects.filter(user1=request.user)
        u.price = y
        u.country = request.POST.get('country')
        u.fname = request.POST.get('fname')
        u.lname = request.POST.get('lname')
        u.address = request.POST.get('address')
        u.code = request.POST.get('code')
        u.contact = request.POST.get('contact')
        u.email = request.POST.get('email')
        u.update()
        return render(request, 'homepage/successful_checkout.html', {'y': y,'cart': cart, 'u': u, 'd': d})
    else:
        return render(request, 'homepage/checkout.html', {'y': y})


def successful_checkout(request):
    return render(request, 'homepage/successful_checkout.html',{})


def DeleteUserItem(request):
    cart = Cart.objects.filter(user=request.user)
    cart.delete()
    return redirect('homepage:index')