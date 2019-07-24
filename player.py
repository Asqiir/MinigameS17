stats = {
    'health':10,
    'max_health':10,
    'alc':5,
    'max_alc':10,
}

inventories = {
}


def activate(consumable):
    stats['health'] += consumable.health_change
    stats['alc'] += consumable.alc_change

def add_inventory(identifier, inventory):
    inventories[identifier] = inventory
