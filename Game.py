from Entities.Player import Player
from Observers.Observer import Observer
from Neighborhood import Neighborhood

class Game(Observer):
    """
    A simple class that hold the player and the Neighborhood and provides
    functionality to interact with them
    """

    def __init__(self):

        self._player = Player()
        self._player.add_observer(self)
        self._playerLoc = (0, 0)
        self._neighborhood = Neighborhood()
        self._isPlaying = True

    def receiveUpdate(self, info=None):
        self._isPlaying = False

    def getStatus(self):
        return self._isPlaying

    def getPlayer(self):
        return self._player

    def getNeighborhood(self):
        return self._neighborhood

    def getPlayerLoc(self):
        return self._playerLoc

    def move(self, dir):

        if not self._isPlaying:
            return False

        valid = [-1, 0, 1]
        if dir[0] in valid and dir[1] in valid:
            newLoc =  (self._playerLoc[0] + dir[0], self._playerLoc[1] + dir[1])
            if self._neighborhood.inBounds(newLoc):
                self._playerLoc = newLoc
                return True
        return False
    
    def attackHouse(self, loc, weaponNum):

        if not self._isPlaying:
            return

        self._player.attackAll(self._neighborhood.getHouse(loc), weaponNum)
        self._neighborhood.getHouse(loc).dealDamage(self._player)
