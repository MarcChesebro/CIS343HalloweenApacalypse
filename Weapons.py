from random import randrange, randint
from Observers.Observable import Observable

# TODO set attack at constructor

class Weapon(Observable):
    """
    Weapon class that holds a weapons attack modifier and Durability
    """
    def __init__(self, durability, attackModifier, name=None):
        self._attackModifier = attackModifier
        self._durability = durability
        self._name = name
        super(Weapon, self).__init__()

    def __str__(self):
        return "{} \t Durability: {}".format(self._name, self._durability)

    def getName(self):
        return self._name

    def use(self, amount):
        if self._durability > 0:
            modAmount = amount * self._attackModifier

            self._durability = self._durability - 1

            return modAmount
        else:
            return -1

    def checkStatus(self):
        if self._durability <= 0:
            self.sendUpdate(self)
            self.remove_all_observers()

class HersheyKisses(Weapon):
    """A basic weapon with unlimited uses and no attack modifier."""
    def __init__(self):
        super(HersheyKisses, self).__init__(1, 1, "Hersey Kisses")

    def use(self, amount):
        modAmount = amount

        self._durability = self._durability - 1
        return modAmount

def generateRandomWeaponList(amount, player):
    weapons = []
    for i in range(amount):
        weapons.append(generateRandomWeapon())
        weapons[len(weapons) - 1].add_observer(player)
    return weapons

def generateRandomWeapon():
    weaponInt = randint(0, 0)
    if(weaponInt == 0):
        return HersheyKisses()
    else:
        return HersheyKisses()
