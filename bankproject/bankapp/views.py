from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect




def home(request):

    return render(request,"base.html")
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid Username or Password")
            return redirect('login')
    return render(request,"login.html")


def register(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']
        cnpassword = request.POST['password1']
        if password == cnpassword:
            if User.objects.filter(username=user).exists():
                messages.info(request, "username taken")
                return redirect('register')

            else:
                newvar = User.objects.create_user(username=user, password=password)

                newvar.save()
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")
def biodata(request):

    return render(request,'biodata.html')



