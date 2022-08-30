from django.db import connections

class PlayerAdd: 

    def __init__(self,username="",fullname="",mobileNumber="",email="",address="") :
        self.username=username
        self.fullname=fullname;
        self.mobileNumber=mobileNumber
        self.email=email
        self.address=address
    
    def addPlayer(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO ritu_web_app_players(username,fullname,mobileNumber,email,address) VALUES('"+self.username+"','"+self.fullname+"','"+self.mobileNumber+"','"+self.email+"','"+self.address+"')")
        