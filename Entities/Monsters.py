from .Entity import Entity
from Weapons import SourStraws, ChocolateBars, NerdBombs
from random import randint

class Person(Entity):

    # constructor that calls Entity's constructor with 100 health and -1
    # damage(to heal for 1 instead of hurting them)
    def __init__(self):
        super(Person, self).__init__(100, -1)

    def __str__(self):
        return "Human"

    # overrides the take damage constructor to take 0 damage from attacks
    def takeDamage(self, amount, weapon):
        super(Person, self).takeDamage(0)

class Zombie(Entity):
    def __init__(self):
        super(Zombie, self).__init__(health=randint(50, 100), attack=randint(0, 10))

    def __str__(self):
        return "Zombie"

    def takeDamage(self, amount, weapon):
        if type(weapon) is SourStraws:
            print("Zombies take Double damage from Sour Straws")
            damage = amount * 2
        else:
            damage = amount

        super(Zombie, self).takeDamage(damage)

class Vampire(Entity):
    """A Vampire Monster that is not harmed by Chocolate bars or SourStraws"""
    def __init__(self):
        super(Vampire, self).__init__(health=randint(100, 200), attack=randint(10, 20))

    def __str__(self):
        return "Vampire"

    def takeDamage(self, amount, weapon):

        if type(weapon) is ChocolateBars:
            print("Vampires take no damage from Chocolate Bars")
            damage = 0
        else:
            damage = amount

        super(Vampire, self).takeDamage(damage)

class Ghoul(Entity):
    """A Ghoul Monster that takes 5X the damage from NerdBombs"""
    def __init__(self):
        super(Ghoul, self).__init__(health=randint(40, 80), attack=randint(15, 30))

    def __str__(self):
        return "Ghoul"

    def takeDamage(self, amount, weapon):
        if type(weapon) is NerdBombs:
            damage = amount * 5
        else:
            damage = amount

        super(Ghoul, self).takeDamage(damage)

class Werewolf(Entity):
    """A Ghoul Monster that takes 5X the damage from NerdBombs"""
    def __init__(self):
        super(Werewolf, self).__init__(health=200, attack=randint(0, 40))

    def __str__(self):
        return "Werewolf"

    def takeDamage(self, amount, weapon):
        if type(weapon) is ChocolateBars or type(weapon) is SourStraws:
            print("Werewolves take no damage from Chocolate Bars or Sour Straws")
            damage = 0
        else:
            damage = amount

        super(Werewolf, self).takeDamage(damage)

def generateRandomMonster():
    monsterInt = randint(0, 4)
    if(monsterInt == 0):
        return Person()
    elif(monsterInt == 1):
        return Zombie()
    elif(monsterInt == 2):
        return Vampire()
    elif(monsterInt == 3):
        return Ghoul()
    elif(monsterInt == 4):
        return Werewolf()
    else:
        return None
