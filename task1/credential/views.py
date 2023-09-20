from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"The User Name already Registerd please try another one")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "The User Name already Registerd please try another one")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()

        else:
            messages.info(request, "please type corr`ect password")
            return redirect('register')
        return redirect('login')
    return render(request,"reg.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"not a user")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return render(request,'index.html')