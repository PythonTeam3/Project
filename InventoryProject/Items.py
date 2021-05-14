class Item:
    def __init__(self,name,stock):
        self.name=name
        self.stock=stock
        self.isLocked=False
        
    def getName(self):
        return self.name
    
    def getStock(self):
        return self.stock
    
    def setStock(self):
        self.stock = self.stock-1
