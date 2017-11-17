from random import uniform, randint
from Observers.Observable import Observable

# TODO set attack at constructor

class Weapon(Observable):
    """
    Weapon class that holds a weapons attack modifier and Durability
    """
    def __init__(self, durability, attackModifier, name=None):
        """
        Constructor to initailize instance variables

        :param durability: Durability of the weapon
        :param attackModifier: attackModifeir when useing the weapon
        :param name: name of the weapon to print out
        """
        self._attackModifier = attackModifier
        self._durability = durability
        self._name = name

        # set up Observer list
        super(Weapon, self).__init__()

    def __str__(self):
        """
        returns a string representation of the weapon
        """
        return "{} \t Durability: {}".format(self._name, self._durability)

    def getName(self):
        """
        return the name of the weaponNum

        :return: the name of the weapon
        """
        return self._name

    def use(self, amount):
        """
        uses the weapon calculating wwapon damge and reducing Durability

        :param amount: base damage to modify
        :return: modified amount of damage
        """
        # first check if durability is greater than 0
        if self._durability > 0:
            # modify amount
            modAmount = amount * self._attackModifier

            # reduce durability
            self._durability = self._durability - 1

            return modAmount
        else:
            return 0

    def checkStatus(self):
        """
        if the weapon has broken remove it from the players inventory
        """
        if self._durability <= 0:
            self.sendUpdate(self)
            self.remove_all_observers()

class HersheyKisses(Weapon):
    """A basic weapon with unlimited uses and no attack modifier."""
    def __init__(self):
        """
        call Weapon constructor with opropriate values
        """
        super(HersheyKisses, self).__init__(1, 1, "Hersey Kisses")

    def use(self, amount):
        """
        override use method to make it so the durability never decreases

        :return: unmodified amount
        """
        modAmount = amount
        return modAmount

class SourStraws(Weapon):
    """Weapon that can be used twice for 1-1.75"""
    def __init__(self):
        """
        call Weapon constructor with opropriate values
        """
        super(SourStraws, self).__init__(2, uniform(1, 1.75), "Sour Straws")

class ChocolateBars(Weapon):
    """Weapon that can be used 4 times for 2-2.4"""
    def __init__(self):
        """
        call Weapon constructor with opropriate values
        """
        super(ChocolateBars, self).__init__(4, uniform(2, 2.4), "Chocolate Bars")

class NerdBombs(Weapon):
    """Weapon that can be used 1 times for 3.5-5"""
    def __init__(self):
        """
        call Weapon constructor with opropriate values
        """
        super(NerdBombs, self).__init__(1, uniform(3.5, 5), "Nerd Bombs")

def generateRandomWeaponList(amount, player):
    """
    generate a random list of Weapons

    :param amount: amount of weapons to generate
    :param player: player that wants to Observer the weapons
    :return: list of random weapons of length amount
    """

    # initialize empty list
    weapons = []
    # generate the weapons and add them to the list
    for i in range(amount):
        weapons.append(generateRandomWeapon())
        # add the player to the weapons observer list
        weapons[len(weapons) - 1].add_observer(player)
    return weapons

def generateRandomWeapon():
    """
    helper function that generates a random weapon

    :return: random weapon
    """
    weaponInt = randint(0, 3)
    if weaponInt == 0:
        return HersheyKisses()
    elif weaponInt == 1:
        return SourStraws()
    elif weaponInt == 2:
        return ChocolateBars()
    elif weaponInt == 3:
        return NerdBombs()
