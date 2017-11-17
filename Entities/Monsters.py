from .Entity import Entity
from Weapons import SourStraws, ChocolateBars, NerdBombs
from random import randint

class Person(Entity):
    """
    A Person Entity that has not been transformed into a monster
    they help the player by healing them instead of dealing damage
    """

    # constructor that calls Entity's constructor with 100 health and -1
    # damage(to heal for 1 instead of hurting them)
    def __init__(self):
        """
        constructor that calls super with strength as -1 to heal instead
        of deal damage and 100 health
        """
        super(Person, self).__init__(100, -1)

    def __str__(self):
        """
        returns a string to represent the object
        """
        return "Human"

    # overrides the take damage constructor to take 0 damage from attacks
    def takeDamage(self, amount, weapon):
        """
        override takeDamage function to take no damage
        """
        super(Person, self).takeDamage(0)

class Zombie(Entity):
    def __init__(self):
        """
        constructor that calls super constructor with default values
        """
        super(Zombie, self).__init__(health=randint(50, 100), attack=randint(0, 10))

    def __str__(self):
        """
        returns a string to represent the object
        """
        return "Zombie"

    def takeDamage(self, amount, weapon):
        """
        override takeDamage function to take double damage from SourStraws
        """
        # if the weapon is SourStraws take double the damage
        if type(weapon) is SourStraws:
            # tell the palyer why damage was doubled
            print("Zombies take Double damage from Sour Straws")
            damage = amount * 2
        else:
            damage = amount

        # call super with final amount
        super(Zombie, self).takeDamage(damage)

class Vampire(Entity):
    """
    A Vampire Monster that is not harmed by Chocolate bars or SourStraws
    """
    def __init__(self):
        """
        constructor that calls super constructor with default values
        """
        super(Vampire, self).__init__(health=randint(100, 200), attack=randint(10, 20))

    def __str__(self):
        """
        returns a string to represent the object
        """
        return "Vampire"

    def takeDamage(self, amount, weapon):
        """
        override takeDamage function to no damage from ChocolateBars
        """
        # check if weapon is a ChocolateBar
        if type(weapon) is ChocolateBars:
            print("Vampires take no damage from Chocolate Bars")
            damage = 0
        else:
            damage = amount

        # call super with the final damage amount
        super(Vampire, self).takeDamage(damage)

class Ghoul(Entity):
    """
    A Ghoul Monster that takes 5X the damage from NerdBombs
    """
    def __init__(self):
        """
        constructor that calls super constructor with default values
        """
        super(Ghoul, self).__init__(health=randint(40, 80), attack=randint(15, 30))

    def __str__(self):
        """
        returns a string to represent the object
        """
        return "Ghoul"

    def takeDamage(self, amount, weapon):
        """
        override takeDamage function to take 5x damage from NerdBombs
        """
        # check if weapon is NerdBombs
        if type(weapon) is NerdBombs:
            damage = amount * 5
        else:
            damage = amount

        # call super with final damage amount
        super(Ghoul, self).takeDamage(damage)

class Werewolf(Entity):
    """
    A Ghoul Monster that takes 5X the damage from NerdBombs
    """
    def __init__(self):
        """
        constructor that calls super constructor with default values
        """
        super(Werewolf, self).__init__(health=200, attack=randint(0, 40))

    def __str__(self):
        """
        returns a string to represent the object
        """
        return "Werewolf"

    def takeDamage(self, amount, weapon):
        """
        override takeDamage function to not take damage from ChocolateBars
        or SourStraws
        """
        # check weapon types and motify values as necessary
        if type(weapon) is ChocolateBars or type(weapon) is SourStraws:
            print("Werewolves take no damage from Chocolate Bars or Sour Straws")
            damage = 0
        else:
            damage = amount

        # call super with final amount
        super(Werewolf, self).takeDamage(damage)

def generateRandomMonster():
    """
    Helper function to generate a random monster
    """
    # generate random in to pick a monster
    monsterInt = randint(0, 4)

    # use randint to pick monster and return it
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
