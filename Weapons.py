from random import uniform, randint
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
        return modAmount

class SourStraws(Weapon):
    """Weapon that can be used twice for 1-1.75"""
    def __init__(self):
        super(SourStraws, self).__init__(2, uniform(1, 1.75), "Sour Straws")

class ChocolateBars(Weapon):
    """Weapon that can be used 4 times for 2-2.4"""
    def __init__(self):
        super(ChocolateBars, self).__init__(4, uniform(2, 2.4), "Chocolate Bars")

class NerdBombs(Weapon):
    """Weapon that can be used 1 times for 3.5-5"""
    def __init__(self):
        super(NerdBombs, self).__init__(1, uniform(3.5, 5), "Nerd Bombs")

def generateRandomWeaponList(amount, player):
    weapons = []
    for i in range(amount):
        weapons.append(generateRandomWeapon())
        weapons[len(weapons) - 1].add_observer(player)
    return weapons

def generateRandomWeapon():
    weaponInt = randint(0, 3)
    if weaponInt == 0:
        return HersheyKisses()
    elif weaponInt == 1:
        return SourStraws()
    elif weaponInt == 2:
        return ChocolateBars()
    elif weaponInt == 3:
        return NerdBombs()
