class Item:
    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

class Consumable(Item):
    def __init__(self, weight, size, health_change, alc_change):
        super().__init(weight, size)
        
        self.health_change = health_change
        self.alc_change = alc_change


class InventoryExplodedError(RuntimeError):
    pass


class Inventory:
    def __init__(self):
        self.content = []
    
    def show_content(self):
        return content
    
    def would_item_fit(self, item):
        raise NotImplentedError()

    def put(self, item):
        if would_item_fit(item):
            content.append(item)
        else:
            raise InventoryExplodedError
    
    def is_accessible(self):
        raise NotImplentedError()



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
    
    def is_accessible(self):
        return True

