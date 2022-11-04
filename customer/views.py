from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login 
from .models import *
from hashlib import sha256
from django.contrib.auth import authenticate,login,logout
from operator import itemgetter


# def register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
#         new_user(username=username,email=email,pass1=pass1).save()
#     elif request.method == "POST":
#         u = request.POST.get('sign_username')
#         p = request.POST.get('sign_password')
#         new=new_user.objects.filter(username=u,pass1=p)
#         if new:
#             return redirect('home')
#         else:
#             return redirect('index')
       
#     return render(request,'customer/index.html')
def register(request):
    if request.method == "POST": 
        if request.POST.get('register') == 'submit':
            username = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if pass1 == "" and username == "" and email == "":
                return redirect('index')
            elif pass1 == pass2:
                new_user(username=username,email=email,password=pass2).save()
                return render(request,"customer/index.html")
            else:
                return redirect('index')          
        elif request.POST.get('login') == 'Login':
            username1 = request.POST.get('sign_username')
            password1 = request.POST.get('sign_password')
            user=new_user.objects.filter(username=username1,password=password1)
            if user:
                return redirect('home')
            else:
                return redirect('index')
    return render(request,"customer/index.html") 
    



        # password2=sha256(password1.encode()).hexdigest()
        # password=sha256(pass2.encode()).hexdigest()


def home(request):
    Trending  = product.objects.filter(trending=1)[:8]
    Black = product.objects.filter(black=1)[:8]
    context = {'Black':Black,'Trending':Trending}
    return render(request,'customer/home.html', context)

def homeview(request, name):
    if(product.objects.filter(name=name)):
        Product = product.objects.filter(name=name).first()
        Random = product.objects.all().order_by('?')[:4]
        context = {'Product':Product,'Random':Random}
        return render(request,'customer/sproduct.html', context)
    else:
        messages.warning(request, "Out of stock")
        return redirect('shop')

def shop(request):
    Product = product.objects.filter()
    context = {'Product':Product}
    return render(request,'customer/shop.html', context)

def shop2(request):
    return render(request,'customer/shop2.html')

def shopview(request, name):
    if(product.objects.filter(name=name)):
        Product = product.objects.filter(name=name).first()
        Random = product.objects.all().order_by('?')[:4]
        context = {'Product':Product,'Random':Random}
        return render(request,'customer/sproduct.html', context)
    else:
        messages.warning(request, "Out of stock")
        return redirect('shop')
    Random = product.objects.all().order_by('?')
    
    
    

def cart(request):
    return render(request,'customer/cart.html')

def customize(request):
    return render(request,'customer/customize.html')

def order(request):
    return render(request,'customer/order.html')

def feedback(request):
    return render(request,'customer/feedback.html')
 
