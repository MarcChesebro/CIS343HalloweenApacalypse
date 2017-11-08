from Entities.Player import Player
from Neighborhood import Neighborhood

class Game(object):

    def __init__(self):
        self.player = Player()
        self.playerLoc = (0, 0)
        self.neighborhood = Neighborhood()
