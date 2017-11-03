from .Entity import Entity
from random import randint

class Person(Entity):

    # constructor that calls Entity's constructor with 100 health and -1
    # damage(to heal for 1 instead of hurting them)
    def __init__(self):
        super(Person, self).__init__(100, -1)

    # overrides the take damage constructor to take 0 damage from attacks
    def takeDamage(amount):
        super(Person, self).takeDamage(0)

class Zombie(Entity):
    def __init__(self):
        super(Zombie, self).__init__(health=randint(50, 100), attack=1)
    def dealDamage(self, target):
        super(Zombie, self).dealDamage(target, randint(0, 10))
