import enum
from operator import add
from tokenize import Double, Intnumber
from xmlrpc.client import DateTime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import addTextTask
from . import updatedLeaderboard
from . import marketPlace
from . import player
from . import orders
from .models import Leaderboard, Marketplace, Players,Messages
from django.core import serializers
from datetime import datetime
from django.contrib import messages
import time

def homepage(request):
    """The home page for ritu"""
    return render(request, 'ritu_web_app/homepage.html')

def aboutUs(request):
    return render(request,'ritu_web_app/aboutUs.html')
def contactUs(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        if(Messages.objects.create(name=name,email=email,message=message)):
            messages.info(request,'Your message is stored successfully')
        else:
            messages.info(request,"An unexpected error occured")
            
    return render(request,'ritu_web_app/contactUs.html')
def finalMessage(request):
    return render(request, 'ritu_web_app/FinalMessege.html')
def showLeaderboard(request):
    
    leaderboard=updatedLeaderboard.Leaderboards()
    data=leaderboard.showLeaderboardTable()
    
    # playerid=[]
    # name=[]
    # earnedPoints=[]
    # for i in range (len(data['data'])):
           
    #     playerid.append(data['data'][i]['playerid']) 
    #     name.append(data['data'][i]['name'])
    #     earnedPoints.append(data['data'][i]['earnedPoints'])    
    
    context={'datas':data,
    }
    print(context)
    #print(context)
    return render(request, 'ritu_web_app/Leaderboard.html',context)

def marketplace(request):
    
    product=marketPlace.Market()
    context=product.showProducts()
    if request.method=="POST":
        productID=request.POST['productID']
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        playerID = request.user.username
        
        order=orders.TrackOrder(playerID,productID,name,address,contact)
        if(order.addOrder()):
            messages.info(request,'Purchase Confirmed!')
        else:
            messages.info(request,'Unexpected Error Occured! Enter correct Product ID')
        
    return render(request, 'ritu_web_app/Marketplace.html',context)

    
def task1(request):
    if request.method=="POST":
        text=request.POST['task_1_url']
        file=request.FILES.get('file')
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_1()
        addingUrl.addTextProof_1(file)
        
        
        #inserting data in leaderboard
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        addingInLeaderboard.insertDataInLeaderboard()
        
        
        
        return redirect('ritu_web_app:task2')

    return render(request, 'ritu_web_app/task1.html')
def task2(request):
    if request.method=="POST":
        text=request.POST['task_2_url']
        file=request.FILES.get('file')
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_2()
        print(file)
        addingUrl.addTextProof_2(file)
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        addingInLeaderboard.insertDataInLeaderboard()
        
        return redirect('ritu_web_app:task3')
    return render(request, 'ritu_web_app/task2.html')
def task3(request):
    if request.method=="POST":
        text=request.POST['task_3_url']
        file=request.FILES.get('file')
        player = request.user.username
        
        #Calculating score
        timeInMilli = int(round(time.time() * 1000)) #getting current time
        
        date_obj = datetime.strptime('01.09.2022 00:00:00,00','%d.%m.%Y %H:%M:%S,%f') #getting the time of when the task was launched 
        endTimeinMilli =int(date_obj.timestamp() * 1000)
        
        gapOfTimeInMilli=endTimeinMilli-timeInMilli #findin the time gap 
        
        point=round(0.00000014452*float(gapOfTimeInMilli),5) #rounding off points to 5 decimal digits
        points=str(point)
        
        #populating table with datas
        addingUrl=addTextTask.TextUrl(points,text,player)
        addingUrl.addTextUrl_3()
        addingUrl.addTextProof_3(file)
        
        addingInLeaderboard=updatedLeaderboard.Leaderboards(player)
        addingInLeaderboard.insertDataInLeaderboard()
        
        return redirect('ritu_web_app:finalMessage')
    return render(request, 'ritu_web_app/task3.html')
def verification(request):
    return render(request,'ritu_web_app/verificationPage.html')
def profileCard(request):
    username = request.user.username
    playerdata=player.Player(username)
    context=playerdata.getInfo()
    
    if request.method=="POST" and request.FILES['picture']:
        file=request.FILES['picture']
        forimage=Players.objects.get(username=username)
        forimage.picture=file
        forimage.save()
        playerdata2=player.Player(username)
        context2=playerdata2.getInfo()
        
        return render(request,'ritu_web_app/profileCard.html',context2)
    
    return render(request,'ritu_web_app/profileCard.html',context)

def FinalMessege(request):
    return render(request,'ritu_web_app/FinalMessege.html')
def order(request):
    return render(request,'order.html')
