#Nathan Hinton
#11/28/2018

#Player class of my game
import random

class player:
    def __init__(self, mult, name):
        mult +=1#So that everything is not 0
        self.name = name
        self.maxLife = 100*mult
        self.maxShields = 100*mult
        self.life = 100*mult
        self.shields = 100*mult
        self.shieldRegenRate = self.maxShields/20*mult
        self.level = 1
        self.levelIncrease = 1.15*mult #Increase stats by %15
        self.attackLevel = 1
        self.xp = 0
        self.nextLevelAt = self.level*10+self.level
    def levelUp(self):
        print()
        self.level += 1
        self.maxLife = round(self.maxLife * self.levelIncrease)
        self.maxShields = round(self.maxShields * self.levelIncrease)
        self.sheildRegenRate = round(self.maxShields/20)
        print("You leveled up!  Here are your new stats:")
        print("Level %s"%str(self.level))
        self.stat()
        print("Shield regeneration rate now: %s"%str(self.sheildRegenRate))
        self.nextLevelAt = self.level*10+self.level
        print("Next level at %s xp."%str(self.nextLevelAt))
    def upgradeAttack(self):
        self.attackLevel += 1
    def attack(self):
        self.i = input("attack (y, n) ")
        if self.i == 'y':
            self.xp += random.randint(0, 100)/10*(.5*self.attackLevel)
            print(random.randint(0, 100)/10*(.5*self.attackLevel))
            return random.randint(0, 100)/10*(.5*self.attackLevel)
        else:
            print('%s chose not to attack'%self.name)
    def getHurt(self, damage):
        self.shields -= damage
        self.xp += damage/10
        if 0>self.shields:
            self.life += self.shields
            self.shields = 0
    def stat(self):
        print("XP: "+str(self.xp))
        #print("Max Life/Sheilds: "+str(self.maxLife))
        print("Current Life: "+str(self.life))
        print("Current Shields: "+str(self.shields))
        #print("current level: "+str(self.level))
    def regen(self):
        self.shields += self.shieldRegenRate
        if self.shields > self.maxShields:
            self.shields = self.maxShields
    def die(self):
        if self.life <=0:
            print(self.life)
            print("%s died"%self.name)
            return True
        else:
            return False
    def update(self, damage):
        print(self.name)
        self.getHurt(damage)
        self.regen()
        self.stat()
        if self.xp>=self.nextLevelAt:
            self.levelUp()

#Testing code.  remove when finished with module
