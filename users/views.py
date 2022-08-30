from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from ritu_web_app import addPlayers

def signupPage(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        username=request.POST['username']
        email=request.POST['email']
        mobileNumber=request.POST['mobileNumber']
        address=request.POST['address']
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')

        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('users:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('users:signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();

                #sending data to the Players table to register the user through addPlayers class
                playerRegistration=addPlayers.PlayerAdd(username, fullname, mobileNumber, email, address)
                playerRegistration.addPlayer()

                return redirect('users:login')
        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('users:signup')
    else:
         return render(request, 'registration/signUpForm.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('users:menu')
        else:
            messages.info(request,'Credentials given are wrong')
            return redirect('users:login')
    else:
        return render(request,'registration/loginPage.html')
def menu(request):
    return render(request,'registration/menu.html')