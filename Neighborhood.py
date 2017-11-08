from House import House

class Neighborhood(object):
    def __init__(self, height=5, width=5):
        self._houses = [[House() for x in range(width)] for y in range(height)]

    def attack(self, source, x, y):
        # tell the player which house to attack and deal damage to all the monsters
        source.dealDamage(self._houses[x][y], 0)
        # have the monster deal damage back
        self._houses[x][y].dealDamage(source)
