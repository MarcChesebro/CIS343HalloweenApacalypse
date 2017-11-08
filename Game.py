from Entities.Player import Player
from Neighborhood import Neighborhood

class Game(object):

    def __init__(self):
        self.player = Player()
        self.playerLoc = (0, 0)
        self.neighborhood = Neighborhood()

        def move(self, dir):
            if dir[0] in range(0, 1) && dir[1] in range(0, 1):
                newLoc =  (self.playerLoc[0] + dir[0], self.playerLoc[1] + dir[1])
                if self.neighborhood.inBounds(newLoc)
                    self.playerLoc = newLoc
