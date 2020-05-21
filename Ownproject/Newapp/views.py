from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Please check your Username and Password')
            return redirect('/')
        else:
            return redirect('Newapp:home')
    else:
        return render(request, 'mytemp/login.html')


def home(request):
    return render(request,'mytemp/home.html')

def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password != cpassword:
            messages.info(request,"Password mismatch")
            return redirect('Newapp:register')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('Newapp:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already taken')
                return redirect('Newapp:register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                messages.success(request, "Succesfully Registered")
                return redirect('/')
    else:
        return render(request, 'mytemp/registration.html')


def user_logout(request):
    logout(request)
    return redirect('/')

def image(request):
    return render(request,'mytemp/photo.html')

def members(request):
    return render(request,'mytemp/members.html')


