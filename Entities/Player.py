from .Entity import Entity
import Weapons

class Player(Entity):

    def __init__(self):
        self._weapons = Weapons.generateRandomWeaponList(10)

    def dealDamage(self, house, weaponNum):
        house.takeDamage(weapons[weaponNum].use(self.attack), weapons[weaponNum])
