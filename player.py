#Nathan Hinton
#11/28/2018

#Player class of my game

class player:
    def __init__(self):
        self.maxLife = 100
        self.maxShields = 100
        self.life = 100
        self.shields = 100
        self.sheildRegenRate = self.maxSheild/20
        self.level = 1
        self.levelIncrease = 1.15 #Increase stats by %15
        self.attackLevel = 1
        self.xp = 0
    def levelUp(self):
        self.level += 1
        self.maxLife = round(self.maxLife * self.levelIncrease)
        self.maxShields = round(self.maxShields * self.levelIncrease)
        self.sheildRegenRate = round(self.maxSheild/20)
    def attack(self):
        pass
    def getHurt(self, damage):
        self.shields -= damage
        if 0>self.shields:
            self.life += self.shields
            self.shields = 0
    def stat(self):
        print("Max Life/Sheilds: "+str(self.maxLife))
        print("Current Life: "+str(self.life))
        print("Current Shields: "+str(self.shields))
        print("current level: "+str(self.level))
    def regen(self):
        self.sheild += self.sheildRegenRate
    def update(self, damage):
        self.regen()
        self.getHurt(damage)
        self.stat()

#Testing code.  remove when finished with module
n = player()
