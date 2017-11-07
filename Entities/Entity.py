from Observers.Observable import Observable

class Entity(Observable):
    def __init__(self, health = 100, attack = 10):
        self._health = health
        self._attack = attack
        super(Entity, self).__init__()

    def isDead(self):
        if _health < 0:
            return True
        return False

    def takeDamage(self, amount, weapon=None):
        self._health = self._health - amount
        print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))


    def dealDamage(self, target, modifier=1):
        target.takeDamage(self._attack * modifier)
