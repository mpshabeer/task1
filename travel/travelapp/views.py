from django.http import HttpResponse
from django.shortcuts import render
from .models import images,teams
# Create your views here.

def demo(request):
    obj = images.objects.all()
    ob=teams.objects.all()
    return render(request,'index.html',{'result':obj,'team':ob})


def additc(request):

    return render(request,'addition.html')

def result(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x + y
    mul=x*y
    sub=x-y
    div=x/y

    return render(request,'result.html',{'obj':res,'mul':mul,'sub':sub,'div':div})

