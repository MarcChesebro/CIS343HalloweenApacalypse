from Entities.Player import Player
from Neighborhood import Neighborhood

class Game(object):
    """
    A simple class that hold the player and the Neighborhood and provides
    functionality to interact with them
    """

    def __init__(self):

        self._player = Player()
        self._playerLoc = (0, 0)
        self._neighborhood = Neighborhood()

    def getPlayerLoc(self):
        return self._playerLoc

    def move(self, dir):

        valid = [-1, 0, 1]
        if dir[0] in valid and dir[1] in valid:
            newLoc =  (self._playerLoc[0] + dir[0], self._playerLoc[1] + dir[1])
            if self._neighborhood.inBounds(newLoc):
                self._playerLoc = newLoc

    def attackHouse(self, loc, weaponNum):
        self._player.attackAll(self._neighborhood.getHouse(loc), weaponNum)
        self._neighborhood.getHouse(loc).dealDamage(self._player)
