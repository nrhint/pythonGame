#Nathan Hinton
#11/28/2018
#11/29/2018
#For attacking

damageTypesClass1 = ['Fire', 'Water', 'Ground', 'Air']
damageTypesClass2 = ['Ranged', 'Melee', 'Pierce', 'Splash']

def check1(i):
    if i in damageTypesClass1:
        return True
    else:
        return False
def check2(i):
    if i in damageTypesClass2:
        return True
    else:
        return False

def damage(baseDamage, dtc1, dtc2):
    if check1(dtc1) == True and check2(dtc2) == True:
        return baseDamage, dtc1, dtc2
    else:
        print("Invalid input to damage in attack.py")

damage(4, 'Fire', 'Ranged')
