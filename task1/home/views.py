from django.http import HttpResponse
from django.shortcuts import render
from home.models import place, Team


# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return HttpResponse("This is About ......................")
def contact(request):
    name = "shabeer"
    return render(request,"contact.html",{'obj':name})

def Details(request):

    return HttpResponse("This is Details ......................")

def thanks(request):
    return render(request,"thanks.html")





def index(request):
    obj=place.objects.all()
    obj2=Team.objects.all()

    return render(request,"index.html",{'obj':obj,'obj2':obj2})






def question(request):
    return render(request,"qpage.html")

def addition(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    result=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return render(request,"result.html",{'res':result,'substraction':sub,'multiplication':mul,'division':div})