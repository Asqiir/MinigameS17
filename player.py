MAX_PORTABLE_SIZE = 10

#Spieler kann das hier einsehen
stats = {
    'health':10,
    'max_health':10,
    'alc':5,
    'max_alc':10,
}

inventories = {
}

hands = {}


#Spieler kann das hier nur austesten / alles im Hintergrund
strength = 10


def activate(consumable):
    stats['health'] += consumable.health_change
    stats['alc'] += consumable.alc_change

def add_inventory(identifier, inventory):
    inventories[identifier] = inventory

def can_hold(item):
    return (len(hands) == 0 and item.weight <= strength and item.size <= MAX_PORTABLE_SIZE) or (len(hands) == 1 and item.weight <= strenght/2 and item.size <= MAX_PORTABLE_SIZE/2)

def hold(item_name, item):
    hands[item_name] = item
