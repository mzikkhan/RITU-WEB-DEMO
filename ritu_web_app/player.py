from audioop import add
from .models import Players,Task1Text,Task2Text,Task3Text
class Player:
    def __init__(self,player):
        self.player=player
    def getInfo(self):
        playerData=Players.objects.raw("SELECT * FROM ritu_web_app_players WHERE username='"+self.player+"'")
        
        task1=Task1Text.objects.raw("SELECT id,earnedPoints FROM ritu_web_app_task1text WHERE player_id='"+self.player+"'")
        getTask1Points=[]
        task1points=0.0
        for task in task1:
            getTask1Points.append(str(task.earnedPoints))
            if(len(getTask1Points)!=0):
                task1points=float(max(getTask1Points))    
        task1time=Task1Text.objects.raw("SELECT id,time_added FROM ritu_web_app_task1text WHERE earnedPoints='"+str(task1points)+"'")
        task1time2=''
        for time in task1time:
            task1time2=time.time_added
        
        task2=Task2Text.objects.raw("SELECT id,earnedPoints FROM ritu_web_app_task2text WHERE player_id='"+self.player+"'")
        getTask2Points=[]
        task2points=0.0
        for task in task2:
            getTask2Points.append(str(task.earnedPoints))
            if(len(getTask2Points)!=0):
                task2points=float(max(getTask2Points))    
        task2time=Task2Text.objects.raw("SELECT id,time_added FROM ritu_web_app_task2text WHERE earnedPoints='"+str(task2points)+"'")
        
        task2time2=''
        for time in task2time:
            task2time2=time.time_added
        
        
        task3=Task3Text.objects.raw("SELECT id,earnedPoints FROM ritu_web_app_task3text WHERE player_id='"+self.player+"'")
        getTask3Points=[]
        task3points=0.0
        for task in task3:
            getTask3Points.append(str(task.earnedPoints))
            if(len(getTask3Points)!=0):
                task3points=float(max(getTask3Points))    
        task3time=Task3Text.objects.raw("SELECT id,time_added FROM ritu_web_app_task3text WHERE earnedPoints='"+str(task3points)+"'")
        task3time2=''
        for time in task3time:
            task3time2=time.time_added
        
        
        username=''
        name=''
        mobileNum=''
        email=''
        address=''
        picture=''
        
        for data in playerData:
            username=data.username
            name=data.fullname
            mobileNum=data.mobileNumber
            email=data.email
            address=data.address
            picture=data.picture
        data={
            'username':username,
            'name':name,
            'mobileNum':mobileNum,
            'email':email,
            'address':address,
            'picture':picture,
            'task1point':task1points,
            'task1time':task1time2,
            'task2point':task2points,
            'task2time':task2time2,
            'task3point':task3points,
            'task3time':task3time2,
        }    
        return data