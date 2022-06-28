from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
import numpy as np
import random
from .import models

def home(request):
    page_title = "Home"
    return render(request, 'home.html', {'page_title': page_title})


def bidding(request):
    page_title = "Bidding"
    return render(request, 'bid.html', {'page_title': page_title})


def features(request):
    page_title = "Features"
    return render(request, 'features.html', {'page_title': page_title})


# Create your views here.
def register(request):
    if request.method == 'POST':
        n = request.POST['user']
        p = request.POST['pass']
        q = request.POST['first']
        r = request.POST['last']
        # s = request.POST['email']
        user = User.objects.create_user(username=n, password=p, first_name=q, last_name=r)
        user.save()
        print("user created")
        #subject = 'Welcome to BAG world'
        #message = f'Hi {user.username}, thank you for registering in our BAG.' \
        #          f'Enter the Verification Code to register'
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list = [user.email]
        #send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("Registered successfully go to login <a href='http://127.0.0.1:8000/login/'>Login<a/>")
    else:
        return render(request, "reg.html")


def user_login(request):
    if request.method == 'POST':
        n = request.POST['user']
        p = request.POST['pass']
        user = auth.authenticate(username=n, password=p)
        if user is not None:
            auth.login(request, user)
            return render(request, "home.html")
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def user_logout(request):
    logout(request)
    return render(request, "home.html")

def verificationcode(request):
    ranvc = random.randint(999,9999)
    if request.method == 'POST':
        c = request.POST['captcha']
        if c == ranvc:
            return render(request, 'login.html',{"ranvc": ranvc})
        else:
            return render(request, 'Codeverification.html', {"ranvc": ranvc})
    return render(request, 'Codeverification.html', {"ranvc": ranvc})

def display(request):
    st1 = models.User1.objects.all()
    # st1=models.User1.objects.values('username')
    return render(request, 'data.html', {'st1': st1})
