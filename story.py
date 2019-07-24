import threading
from . import player
from . import lib

def show_all_options():
    print('Du hast folgende Befehle zur Verfügung:')
    
    for s in reactions:
        print(s)

def show_status():
    print(str(stats['health']) + '/' + str(player.stats['max_health']) + ' Leben')
    print(str(stats['alc']) + '/' + str(player.stats['max_alc']) + ' Alkoholgehalt')

reactions = {
    'befehle':show_all_options,
    'status':show_status,
    'lager':show_lager,
}

def answerinput(given_input):
    if given_input in reactions:
        reactions[textin]()
    else:
        print('Die Eingabe konnte nicht interpretiert werden. Gib »befehle« ein für eine Übersicht über alle Befehle.')
    print()


def gameloop():
    while not gameover:
        textin = input('')
        answerinput(textin)
        

def run():        
    
    print('Du bist Sternenkriegerin, die siebzehnte ihres Namens.')
    print('Du sollst deinem Namen Ehre machen, sprach dein Vater, als er dir die Laserpistole gab.')
    print('Er vergaß die Patronen.')
    print('Du nahmst die Waffe, verbeugtest dich und stiegst in dein Schiff.')
    print('Seit jenem Tag bist du auf der Suche nach Abenteurn, um dich deines Namens würdig zu erweisen.')
    print('So wie deine fünfzehn Schwestern, denn die Galaxis ist friedliebend, und hat kaum Abenteuer zu bieten.')
    print('Nur die erste sucht nicht mehr, denn sie wurde zurückgerufen, den Thron zu übernehmen, als die Mutter starb.')
    print()
    print('Das Schiff ist rostig, du bist weit entfernt von daheim, in der Kabine stapeln sich die leeren Sterni-flaschen, die Mission ist fast vergessen und DEIN ALKOHOL IST ALLE.')
    print()
    print('Tippe »status« um deinen aktuellen Status zu erhalten.')
    
    textin = ''
    
    while not textin == 'status':  
        textin = input('')
        answerinput(textin)    
    
    print('Du spürst, dass du den Alkohol brauchst.')
    print('Schau in deiner Hosentasche nach.')
    print('Vielleicht kannst du dir noch welchen kaufen.')
    print('Tippe »hosentasche« um reinzuschauen, was noch da ist')
    
    player.add_inventory('hosentasche', lib.PortableInventory(
    
    textin = ''
    
    while not textin == 'hosentasche':
        textin = input('')
        answerinput(textin)
    
    game = threading.Thread(target=gameloop)
    game.start()
    
    
gameover = False
    

run()
