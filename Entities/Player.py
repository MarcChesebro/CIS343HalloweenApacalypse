from .Entity import Entity
import Weapons

class Player(Entity):

    def __init__(self):
        self._weapons = Weapons.generateRandomWeaponList(10)
        super(Player, self).__init__()

    def dealDamage(self, house, weaponNum):
        house.takeDamage(self._weapons[weaponNum].use(self._attack), self._weapons[weaponNum])
