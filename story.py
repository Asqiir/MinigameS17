import threading
import player
import lib
import game
        

def run():        
    
    print('Du bist Sternenkriegerin, die siebzehnte ihres Namens.')
    print('Du sollst deinem Namen Ehre machen, sprach dein Vater, als er dir die Laserpistole gab.')
    print('Er vergaß die Patronen.')
    print('Du nahmst die Waffe, verbeugtest dich und stiegst in dein Schiff.')
    print('Seit jenem Tag bist du auf der Suche nach Abenteurn, um dich deines Namens würdig zu erweisen.')
    print('So wie deine fünfzehn Schwestern, denn die Galaxis ist friedliebend, und hat kaum Abenteuer zu bieten.')
    print('Nur die erste sucht nicht mehr, denn sie wurde zurückgerufen, den Thron zu übernehmen, als die Mutter starb.')
    print()
    print('Das Schiff ist rostig und alt, du bist weit entfernt von daheim, die leeren Sterni-flaschen Stapeln sich auf dem Gang, die Mission ist fast vergessen und DEIN ALKOHOL IST ALLE.')
    print()
    print('Tippe »status« um deinen aktuellen Status zu erhalten.')
    
    textin = ''
    
    while not textin == 'status':  
        textin = input('')
        game.answerinput(textin)    
    
    print('Du spürst, dass du den Alkohol brauchst.')
    print('Schau in deiner Hosentasche nach.')
    print('Vielleicht kannst du dir noch welchen kaufen.')
    print('Tippe »hosentasche« um reinzuschauen, was noch da ist')
    
    player.add_inventory('hosentasche', lib.PortableInventory(10,3))
    player.inventories['hosentasche'].put('flachmann', lib.Bottle(1))
    player.inventories['hosentasche'].content['flachmann'].fill(1,lib.Consumable(1,1,0,5))
    
    textin = ''
    
    while not textin == 'hosentasche':
        textin = input('')
        
        if textin != 'nimm flachmann aus hosentasche':
            game.answerinput(textin)
        else:
            print('noch nicht')
            print()

    print('Hast du deinen Flachmann gefunden?')
    print('Nimm ihn dir')
    print('»nimm flachmann aus hosentasche«')
    
    textin == ''
    
    while not textin == 'nimm flachmann aus hosentasche':
        textin = input('')
        game.answerinput(textin)
    
    print('Der Durst wird stärker.')
    print('Trink!')
    
    textin = ''
    fail_counter = 0
    
    while not textin == 'trinke aus flachmann':
        if fail_counter >= 6:
            print('Probier es so: »trinke aus flachmann«')
        elif fail_counter >= 4:
            print('Der Befehl ist »trinke aus <gegenstand>«')
        elif fail_counter >= 2:
            print('Vielleicht kann dir die Befehlsübersicht ja helfen.')
    
        textin = input('')
        game.answerinput(textin)
        fail_counter += 1
        
        
    print('Besser')
    print('Du kannst die Veränderung im Status einsehen')
    print('Komm mit »fertig« zurück zum Tutorial')
    
    textin = ''
    
    while not textin == 'fertig':
        textin = input('')
        if textin != 'fertig':
            game.answerinput(textin)
    
    print('Der Schädel brummt noch ein wenig, du kannst aber wieder klarer denken.')
    print('Du bist Sternenkriegerin, die 17. ihres Namens! Der Stolz des herrschenden Clans!')
    
    threading.Thread(target=game.loop).start()
    
    

    

run()
