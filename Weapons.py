from random import randrange, randint

class Weapon:
    def __init__(self, durability, attackModifierMin, attackModifierMax, name=None):
        self._attackModifierMin = attackModifierMin
        self._attackModifierMax = attackModifierMax
        self._durability = durability
        self._name = name

    def __str__(self):
        return "{} \t Durability: {}".format(self._name, self._durability)

    def use(self, amount):
        modAmount = amount * randrange(self._attackModifierMin, self._attackModifierMax)

        self._durability = self._durability - 1
        return modAmount


class HersheyKisses(Weapon):
    """A basic weapon with unlimited uses and no attack modifier."""
    def __init__(self):
        super(HersheyKisses, self).__init__(1, 1, 1, "Hersey Kisses")

    def use(self, amount):
        modAmount = amount

        self._durability = self._durability - 1
        return modAmount

def generateRandomWeaponList(amount):
    weapons = []
    for i in range(amount):
        weapons.append(generateRandomWeapon())
    return weapons

def generateRandomWeapon():
    weaponInt = randint(0, 0)
    if(weaponInt == 0):
        return HersheyKisses()
    else:
        return HersheyKisses()
