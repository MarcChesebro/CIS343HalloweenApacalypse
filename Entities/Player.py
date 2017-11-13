from .Entity import Entity
from Observers.Observer import Observer
from random import randint
import Weapons

# TODO have player/House interaction be nicer

class Player(Entity, Observer):

    def __init__(self, name="Marc"):
        self._name = name
        self._weapons = Weapons.generateRandomWeaponList(10, self)
        Entity.__init__(self, attack=randint(10, 20))

    def __str__(self):
        return self._name

    def receiveUpdate(self, info):
        if info in self._weapons:
            print("{} durability reaches 0 and falls apart!".format(info.getName()))
            self._weapons.remove(info)

    def attackAll(self, house, weaponNum):
        monsters = house.getMonsterlist()
        damage = self._weapons[weaponNum].use(self._attack)
        for mon in monsters:
            mon.takeDamage(damage, self._weapons[weaponNum])
        self._weapons[weaponNum].checkStatus()

    def dealDamage(self, target, weaponNum):
        target.takeDamage(self._weapons[weaponNum].use(self._attack), self._weapons[weaponNum])

    def printWeapons(self):
        [print("{}: {}".format(i, weap)) for i, weap in enumerate(self._weapons)]

    def getWeapon(self, weaponNum):
        return self._weapons[weaponNum]
