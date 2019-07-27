import errors
import lib
import player

gameover = False

def show_all_options():
    print('Du hast folgende Befehle zur Verfügung:')
    
    print('befehle')
    print('status')
    
    for inventory_name in player.inventories:
        print(inventory_name)

    #for portal_name in rooms.current.portals:
    #   print('gehe zu ' + portal_name)

    print('nimm <gegenstand> aus <inventar>')
    print('trinke aus <gegenstand>')
    
    #print('raum')    

    #for inventory_name in rooms.current.inventories:
    #   print(inventory_name)
    
    #for npc_name in rooms.current.nps:
    #   print('sprich ' + nps_name + ' an')
    
    #for machine_name in rooms.current.machines:
    #   print('nutze ' + machine_name)


def show_status():
    print(str(player.stats['health']) + '/' + str(player.stats['max_health']) + ' Leben')
    print(str(player.stats['alc']) + '/' + str(player.stats['max_alc']) + ' Alkoholgehalt')

def show_inventory(name):
    for item_name in player.inventories[name].content:
        print(item_name)

def is_take_from_player_inventory_statement(string):
    words = string.split(' ')
    if len(words) != 4 or words[0] != 'nimm' or words[2] != 'aus':
        return False
    
    return words[3] in player.inventories and words[1] in player.inventories[words[3]].content
    
def is_drink_statement(string):
    words = string.split(' ')
    return len(words) == 3 and words[0] == 'trinke' and words[1] == 'aus' and words[2] in player.hands and isinstance(player.hands[words[2]], lib.Bottle)

def take_item_from_inventory(inventory, item_name):
    item = inventory.content[item_name]
    
    if player.can_hold(item):
        inventory.remove(item_name)
        player.hold(item_name, item)
        
    else:
        print('Diesen Gegenstand kannst du gerade nicht in die Hand nehmen.')


def answerinput(given_input):
    if given_input == 'befehle':
        show_all_options()
    elif given_input == 'status':
        show_status()
    elif given_input in player.inventories:
        show_inventory(given_input)
    elif is_take_from_player_inventory_statement(given_input):
        inventory = player.inventories[given_input.split(' ')[3]]
        item = given_input.split(' ')[1]

        take_item_from_inventory(inventory, item)        
    elif is_drink_statement(given_input):
        bottle = player.hands[given_input.split(' ')[2]]
        player.activate(bottle.content)
        bottle.empty(1)
        
    else:
        print('Die Eingabe konnte nicht interpretiert werden. Gib »befehle« ein für eine Übersicht über alle Befehle.')
    print()


def loop():
    while not gameover:
        textin = input('')
        answerinput(textin)
