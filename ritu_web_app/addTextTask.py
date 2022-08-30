from operator import imod
from sqlite3 import Cursor
from django.db import connections
from . models import Task1Proof,Task2Proof,Task3Proof
class TextUrl: 

    def __init__(self,points,text="", player="") :
        self.text=text
        # self.time_added=time_added
        self.player=player
        self.points=points
    
    def addTextUrl_1(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task1text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
        
    def addTextProof_1(self,mediaFile):
        self.proof=mediaFile
        Task1Proof.objects.create(player_id=self.player,proof=mediaFile)
    
    def addTextUrl_2(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task2text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
        
    def addTextProof_2(self,mediaFile):
        self.proof=mediaFile
        Task2Proof.objects.create(player_id=self.player,proof=mediaFile)
    
    def addTextUrl_3(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_task3text(text,player_id,earnedPoints) VALUES('"+self.text+"','"+self.player+"','"+self.points+"')")
    
    def addTextProof_3(self,mediaFile):
        self.proof=mediaFile
        Task3Proof.objects.create(player_id=self.player,proof=mediaFile)
    