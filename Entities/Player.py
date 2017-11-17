from .Entity import Entity
from Observers.Observer import Observer
from Observers.Observable import Observable
from random import randint
import Weapons

# TODO have player/House interaction be nicer

class Player(Entity, Observer, Observable):
    """
    The player of the game.
    is an entity and uses its functions for attacking and taking dealDamage
    is an Observer to observe its weapons to see when they break
    is Observable to be Observed by the game so when the player dies
    the game will end
    """
    def __init__(self, name="Player"):
        """
        Constructor to initialize default values and call the Entity and
        Observable constructors to set up values
        """
        self._name = name
        self._weapons = Weapons.generateRandomWeaponList(10, self)
        # call parent constructors
        Entity.__init__(self, attack=randint(10, 20))
        Observable.__init__(self)

    def __str__(self):
        """
        returns a string to represent the object
        """
        return self._name

    def receiveUpdate(self, info):
        """
        Override recieveUpdate function
        if the update contained a weapon assume it has broken and remove it from
        the players inventory
        """
        if info in self._weapons:
            print("{} durability reaches 0 and falls apart!".format(info.getName()))
            self._weapons.remove(info)

    def attackAll(self, house, weaponNum):
        """
        helper function for attacking a house
        takes a house and makes the player attack every monster in the house

        :param house: House that contains the monsters to attack
        :param weaponNum: weapon to use
        """
        monsters = house.getMonsterlist()
        damage = self._weapons[weaponNum].use(self._attack)
        for mon in monsters:
            mon.takeDamage(damage, self._weapons[weaponNum])
        self._weapons[weaponNum].checkStatus()

    def dealDamage(self, target, weaponNum):
        """
        override dealDamage from entity and modify attack by a weaopn
        :param target: Entitiy to attack
        :param weaponNum: weapon to use
        """
        target.takeDamage(self._weapons[weaponNum].use(self._attack), self._weapons[weaponNum])

    def printWeapons(self):
        """
        print the players inventory to the screeen
        """
        [print("{}: {}".format(i, weap)) for i, weap in enumerate(self._weapons)]

    def getWeapon(self, weaponNum):
        """
        get a weapon from the players inventory

        :param weaponNum: index of weapon to grab
        :return: weapon in inventory slot WeaponNum
        """
        return self._weapons[weaponNum]
