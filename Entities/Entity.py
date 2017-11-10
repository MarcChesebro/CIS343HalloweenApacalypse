from Observers.Observable import Observable

class Entity(Observable):
    def __init__(self, health = 100, attack = 10):
        self._health = health
        self._attack = attack
        super(Entity, self).__init__()

    def sendUpdate(self):
        super(Entity, self).sendUpdate(info=self)

    def isDead(self):
        if self._health <= 0:
            return True
        return False

    def takeDamage(self, amount, weapon=None):
        self._health = self._health - amount
        if not self.isDead():
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
        else:
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
            print("{} is defeated and transforms back into a human!".format(self))
            self.sendUpdate()
            self.remove_all_observers()

    def dealDamage(self, target, modifier=1):
        target.takeDamage(self._attack * modifier)
