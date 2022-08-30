from .models import Marketplace

class Market:
    def __init__(self):
        pass
    def showProducts(self):
        
        product=Marketplace.objects.all().values()
        context={
            'productData':product
        }
        
        
       
        
        return context