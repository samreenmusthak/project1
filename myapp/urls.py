from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='index'),
    path('test',views.signup,name='index'),

]