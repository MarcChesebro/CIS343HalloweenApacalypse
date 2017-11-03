from Entity import Entity

class Person(Entity):

    # constructor that calls Entity's constructor with 100 health and -1
    # damage(to heal for 1 instead of hurting them)
    def __init__(self):
        super(Person, self).__init__(100, -1)

    # overrides the take damage constructor to take 0 damage from attacks
    def takeDamage(amount):
        super(Person, self).takeDamage(0)
