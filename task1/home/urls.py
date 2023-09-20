from django.urls import path

from home import views

urlpatterns = [

path('',views.home,name='home'),
path('contact',views.contact,name='contact'),
path('Details',views.Details,name='Details'),
path('about',views.about,name='about'),
path('thanks',views.thanks,name='thanks'),
path('question',views.question,name='question'),
path('addition',views.addition,name='addition'),
path('index',views.index,name='index'),
]