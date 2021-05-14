from Items import *
from Exceptions import *

class Inventory:
    
    item_list = []
    item1 = Item("Phone",2)
    item2 = Item("TV",3)
    item3 = Item("PC",0)
    item_list.append(item1)
    item_list.append(item2)
    item_list.append(item3)
    
    def lock(self,item_type):
        for i in self.item_list:
            if item_type == i.getName():
                i.isLocked = True
    
    def unlock(self,item_type):
        for i in self.item_list:
            if item_type == i.getName():
                i.isLocked = False
    
    def purchase(self,item_type):
        for i in self.item_list:
            if item_type == i.getName():
                if i.isLocked == False:
                    raise ItemNotLocked()
                if i.getStock() < 1:
                    raise OutOfStock()
                else:
                    i.setStock()
                    return i.getStock()
        raise ItemNotFound()   
    
    
