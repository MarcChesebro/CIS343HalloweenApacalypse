from .Entity import Entity
import Weapons

class Player(Entity):

    def __init__(self, name="Marc"):
        self._name = name
        self._weapons = Weapons.generateRandomWeaponList(10)
        super(Player, self).__init__()

    def __str__(self):
        return self._name

    def dealDamage(self, house, weaponNum):
        house.takeDamage(self._weapons[weaponNum].use(self._attack), self._weapons[weaponNum])

    def printWeapons(self):
        [print("{}: {}".format(i, weap)) for i, weap in enumerate(self._weapons)]
