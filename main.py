#Nathan Hinton
#11/28/2018

#Main handler for game

#import files
import player

#Setup players:
n = player.player(0, 'n')
j = player.player(0, 'j')
players = [n, j]


#Main loop:
while len(players) > 0:#while there are players:
    for x in players:
        print()
        print("Player %s's turn."%x.name)
        x.update(20)
        x.attack()
        if x.die():
            players.remove(x)
