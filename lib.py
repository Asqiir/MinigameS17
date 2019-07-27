#from .errors import *
from errors import *

class Item:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

class Consumable(Item):
    def __init__(self, weight, size, health_change, alc_change):
        super().__init__(weight, size)
        
        self.health_change = health_change
        self.alc_change = alc_change



class Bottle(Item):
    def __init__(self, size):
        super().__init__(0, size)
        self.amount = 0
        self.content = None
    
    def fill(self, amount, consumable):
        if self.content == None:
            self.content = consumable
            self.amount = amount        
        elif (self.amount + amount <= self.size) and (self.content == None or self.content.equals(consumable)):
            self.amount += amount
        else:
            raise BottleExplodedError()
    
    def empty(self, amount):
        self.amount -= amount
        
        if self.amount <= 0:
            self.amount = 0
            self.content = None


class Inventory:
    def __init__(self):
        self.content = {}
    
    def show_content(self):
        return content
    
    def would_item_fit(self, item):
        raise NotImplentedError()

    def put(self, name, item):
        if self.would_item_fit(item):
            self.content[name] = item
        else:
            raise InventoryExplodedError
        
    def remove(self, name):
        del self.content[name]


class PortableInventory(Inventory):
    def __init__(self, weight, size):
        super().__init__()
        self.weight = weight
        self.size = size
    
    def __get_total_content_size(self):
        return sum(item.size for item in self.content)
    
    def __get_total_content_weight(self):
        return sum(item.weight for item in self.content)
    
    def would_item_fit(self, item):
        return self.__get_total_content_weight() + item.weight <= self.weight and self.__get_total_content_size() + item.size <= self.size
    
    
