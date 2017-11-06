
class Entity(object):
    def __init__(self, health = 100, attack = 10):
        self._health = health
        self._attack = attack

    def takeDamage(self, amount, weapon=None):
        self._health = self._health - amount
        print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))


    def dealDamage(self, target, modifier=1):
        target.takeDamage(self._attack * modifier)
