from  . import views
from django.urls import path, include

urlpatterns = [
    path('',views.demo,name='demo'),
    path('call',views.additc,name='addict'),
    path('addit/', views.result, name='additc'),
    # path('result/', views.result, name='result'),
]
