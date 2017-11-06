from House import House

class Nieghborhood(object):
    def __init__(self, hieght=5, width=5):
        self._houses = [[House() for x in range(width)] for y in range(hieght)]

    def attack(self, source, x, y):
        # tell the player which house to attack and deal damage to all the monsters
        source.dealDamage(_houses[x][y])
        # loop through monsters in the house and see if any died(health < 0)
        # if it is tell the house to replace it with a Person
