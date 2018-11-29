#Nathan Hinton
#11/28/2018

#Main handler for game

#import files
import player
##import attack
from time import sleep

#Define stuff
def newScreen():
    for x in range(0, 40):
        print()

#Setup players:
setupPlayer = True
p = 0
players = {}
while setupPlayer == True:
    value = player.player(0, input("Player Name: "))
    key = p
    players[key] = value
    p += 1
    if str(input("Finished (y, n):  ")) == 'y':
        setupPlayer = False
#Setup bad guys:
setupPlayer = True
p = 0
targets = {}
while setupPlayer == True:
    value = player.player(-0.5, input("target Name: "))
    key = p
    targets[key] = value
    p += 1
    if str(input("Finished (y, n):  ")) == 'y':
        setupPlayer = False


#Main loop:
while len(players) > 0:#while there are players:
    for x in range(len(players)):
        newScreen()
        print("Player %s's turn."%players[x].name)
        players[x].update(10)
        info = players[x].attack(targets)
        print(info)
        targets[int(info[1])].update(info[0])
        if players[x].die():
            players.pop(x)
        print("Press enter to continue.")
        input()
