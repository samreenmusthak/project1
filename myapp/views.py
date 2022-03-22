from django.shortcuts import render
from django.http import HttpResponse
from .models import users
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        password=request.POST['password']
        address=request.POST['address']
        age=request.POST['age']
        userdata=users(username=username,password=password,fullname=fullname,address=address,age=age)
        userdata.save()

        return render(request,'login.html')
    else:
        return render(request,'login.html')



