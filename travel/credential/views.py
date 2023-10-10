from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    return render(request,'login.html')




def register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email = request.POST['email']
        password=request.POST['pass']
        cnfpassword = request.POST['cnfpass']

        if password==cnfpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'already used this mail')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
                user.save()
                print('registration completed')
                return HttpResponse('''<script>alert("registration compleated");window.location='/cred/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("password not matching");window.location='/cred/register/'</script>''')
    return render(request,'student register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')