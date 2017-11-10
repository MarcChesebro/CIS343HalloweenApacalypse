from House import House

class Neighborhood(object):
    def __init__(self, height=5, width=5):
        self._houses = [[House() for x in range(width)] for y in range(height)]

    def attack(self, source, weapon, x, y):
        # tell the player which house to attack and deal damage to all the monsters
        self._houses[x][y].attackAll(source, weapon)
        # have the monster deal damage back
        self._houses[x][y].dealDamage(source)

    def getHouse(self, loc):
        return self._houses[loc[0]][loc[1]]

    def inBounds(self, loc):
        if loc[0] in range(0, len(self._houses)) and loc[1] in range(0, len(self._houses[0])):
            return True
        else:
            return False
