from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bankingapp.models import Application
from .forms import ApplicationForm
from django import forms
def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'form.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if not username or not password or not cpassword:
            messages.error(request, "Please fill in all the fields")
            return redirect('register')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"passwords not matching")
            return redirect('register')
    return render(request,'register.html')
def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Application successful',fail_silently=True)
            #return redirect('success_page')
    else:
        form = ApplicationForm()
    storage = messages.get_messages(request)
    storage.used = True
    return render(request,'form.html',{'form': form})
def logout(request):
    auth.logout(request)
    return redirect('/')


