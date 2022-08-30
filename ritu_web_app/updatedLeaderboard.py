from django.db import connections
from .models import Leaderboard, Task1Text,Task2Text,Task3Text,Players

class Leaderboards:
    def __init__(self,username=''):
        self.username=username
    
    def insertDataInLeaderboard(self):
        
        playerDetails=Players.objects.raw("SELECT username, fullname FROM ritu_web_app_players WHERE username='"+self.username+"'")
        name=''
        for name in playerDetails:
            name=name.fullname
        
        
        #checking if the player is already in the leaderboard
        
        
        findingPlayer=Leaderboard.objects.raw("SELECT id, player_id FROM ritu_web_app_leaderboard WHERE player_id='"+self.username+"'")
        playername=''
        
        for player in findingPlayer:
            playername=player.player_id
            
        
        #chcking whether the player exists in leaderboard
        
        if (playername==""):
                
                #getting points for particular user from task1 table
                
                task1=Task1Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task1text WHERE player_id='"+self.username+"'")
                getTask1Points=[]
                task1points=0.0
                for task in task1:
                    getTask1Points.append(str(task.earnedPoints))
                if(len(getTask1Points)!=0):
                    task1points=float(max(getTask1Points))
                
            
                #getting points for particular user from task2 table
                task2=Task2Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task2text WHERE player_id='"+self.username+"'")
                getTask2Points=[]
                for task in task2:
                    getTask2Points.append(str(task.earnedPoints))
                task2points=0.0
                if(len(getTask2Points)!=0):
                    task2points=float(max(getTask2Points))
                
                
                #getting points for particular user from task3 table
                task3=Task3Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task3text WHERE player_id='"+self.username+"'")
                getTask3Points=[]
                for task in task3:
                    getTask3Points.append(str(task.earnedPoints))
                task3points=0.0
                if(len(getTask2Points)!=0):
                    task3points=float(max(getTask2Points))
                
                
                leaderboardPoint=round((task1points+task2points+task3points),5)
                print(f"Leaderboard Point: {leaderboardPoint}")
                db_cursor=connections['default'].cursor()
                db_cursor.execute("INSERT INTO ritu_web_app_leaderboard(earnedPoints,player_id,name)VALUES('"+str(leaderboardPoint)+"','"+self.username+"','"+name+"' )")
        
        
        
        else:  #if the player is already in the leaderboard
            
            #getting points for particular user from task1 table
                task1=Task1Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task1text WHERE player_id='"+self.username+"'")
                getTask1Points=[]
                for task in task1:
                    getTask1Points.append(str(task.earnedPoints))
                
                task1points=float(max(getTask1Points))
                
                
                
                #getting points for particular user from task2 table
                task2=Task2Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task2text WHERE player_id='"+self.username+"'")
                getTask2Points=[]
                for task in task2:
                    getTask2Points.append(str(task.earnedPoints))
                task2points=0.0
                if(len(getTask2Points)!=0):
                    task2points=float(max(getTask2Points))
                
                
                
                #getting points for particular user from task3 table
                task3=Task3Text.objects.raw("SELECT id,player_id, earnedPoints FROM ritu_web_app_task3text WHERE player_id='"+self.username+"'")
                getTask3Points=[]
                for task in task3:
                    getTask3Points.append(str(task.earnedPoints))
                task3points=0.0
                if(len(getTask2Points)!=0):
                    task3points=float(max(getTask2Points))
                
                
                
                leaderboardPoint=round((task1points+task2points+task3points),5)
                
                
                db_cursor=connections['default'].cursor()
                db_cursor.execute("UPDATE ritu_web_app_leaderboard SET earnedPoints='"+str(leaderboardPoint)+"' WHERE player_id='"+self.username+"'")
        
    
    def showLeaderboardTable(self):
        #getting data from leaderboard
        standing=Leaderboard.objects.raw("SELECT * FROM ritu_web_app_leaderboard ORDER BY earnedPoints DESC")
        playerid=''
        name=''
        earnedPoints=''
        leaderboardList=[]
        for standing in standing:
            playerid=standing.player_id
            name=standing.name
            earnedPoints=standing.earnedPoints
            
            leaderboardData={'playerid':playerid,'name':name,'earnedPoints':earnedPoints}
            leaderboardData['playerid']=playerid
            leaderboardData['name']=name
            leaderboardData['earnedPoints']=earnedPoints
            leaderboardList.append(leaderboardData)  
        return(leaderboardList)
        
                       