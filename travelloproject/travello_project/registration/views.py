from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        pword=request.POST['pword']
        user=auth.authenticate(username=uname,password=pword)
        if user is not None:
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    return render(request,'login.html')
def register(request):

    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pword = request.POST['pword']
        cpword=request.POST['cpword']
        if pword==cpword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:

                user=User.objects.create_user(username=uname,email=email,password=pword,first_name=fname,last_name=lname)
                user.save()
                return redirect('login')
            print("user created")
        else:
            messages.info(request,'Password not matching')
            print("password not match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')






