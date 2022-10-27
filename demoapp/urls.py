from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.main,name='main'),
    path('second',views.second,name='second')
    ]