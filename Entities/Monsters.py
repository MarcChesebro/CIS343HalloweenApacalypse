from .Entity import Entity
from random import randint

class Zombie(Entity):
    def __init__(self):
        super(Zombie, self).__init__(health=randint(50, 100), attack=1)
    def dealDamage(self, target):
        super(Zombie, self).dealDamage(target, randint(0, 10))
