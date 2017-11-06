from random import randrange, randint

class Weapon:
    def __init__(self, durability, attackModifierMin, attackModifierMax):
        self._attackModifierMin = attackModifierMin
        self._attackModifierMax = attackModifierMax
        self._durability = durability

    def use(self, amount):
        modAmount = amount * randrange(self._attackModifierMin, self._attackModifierMax)

        durability = durability - 1


class HersheyKisses(Weapon):
    """A basic weapon with unlimited uses and no attack modifier."""
    def __init__(self):
        super(HersheyKisses, self).__init__(1, 1, 1)

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
