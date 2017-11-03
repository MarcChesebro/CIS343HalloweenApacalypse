
class Entity(object):
    def __init__(self, health = 100, attack = 10):
        self.health = health
        self.attack = attack

    def takeDamage(self, amount):
        self.health = self.health - amount

    def dealDamage(self, target, modifier=1):
        target.takeDamage(self.attack * modifier)
