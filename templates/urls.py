from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('login',views.index,name='login'),
    path('register',views.index,name='register'),
    path('logout',views.index,name='logout')
]