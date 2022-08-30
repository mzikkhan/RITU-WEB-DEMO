from . models import OrderData,Marketplace
from django.db import connections
class TrackOrder:
    def __init__(self,playerID,productID,customername='',address='',contact='') :
        self.playerID=playerID
        self.productID=productID
        self.customerName=customername
        self.address=address
        self.contact=contact
    def addOrder(self):
        db_cursor=connections['default'].cursor()
        getProduct=Marketplace.objects.raw("SELECT * FROM ritu_web_app_marketplace WHERE id='"+self.productID+"'")
        productName=''
        productPrice=''
        for product in getProduct:
            productName=product.product_name
            productPrice=product.product_price
        
        #for user
        f=True
        
        if(db_cursor.execute("INSERT INTO ritu_web_app_orders (playerID_id,productID_id) VALUES ('"+self.playerID+"','"+self.productID+"')")):
            f=True
        else:
            f=False
        
        #admin database
        if(db_cursor.execute("INSERT INTO ritu_web_app_orderdata (playerName,productid,product_name,productPrice,deliveryAddress,contactNum,playerID_id) VALUES('"+self.customerName+"','"+self.productID+"','"+productName+"','"+productPrice+"','"+self.address+"','"+self.contact+"','"+self.playerID+"')")):
            f=True
        else:
            f=False
        return f
        