from Entities.Player import Player
from Observers.Observer import Observer
from Neighborhood import Neighborhood

class Game(Observer):
    """
    A simple class that hold the player and the Neighborhood and provides
    functionality to interact with them
    """

    def __init__(self, playerName="Player"):
        """
        Constructor that initializes instance variables
        """

        self._player = Player(name=playerName)
        self._player.add_observer(self)
        self._playerLoc = (0, 0)
        self._neighborhood = Neighborhood()
        self._isPlaying = True

    def receiveUpdate(self, info=None):
        """
        override abstract method from Observer.
        when an update is recieved the player has died so end the game

        :param info: info to process
        """
        self._isPlaying = False

    def getStatus(self):
        """
        :return: if the game is still going
        """
        return self._isPlaying

    def getPlayer(self):
        """
        :return: the player of the game
        """
        return self._player

    def getNeighborhood(self):
        """
        :return: the neighborhood of the game
        """
        return self._neighborhood

    def getPlayerLoc(self):
        """
        :return: the players location in (x, y)
        """
        return self._playerLoc

    def move(self, dir):
        """
        move the player. must be a valid move(1 square away including diagonals)

        :param dir: direction to move in a tuple of length 2 with values of
        -1 to 1

        :return: True if move was successful or False if it was not.
        """

        # if the game is over return
        if not self._isPlaying:
            return False

        # valid values for moves
        valid = [-1, 0, 1]

        # if the direction is in the valid range calculat the new location
        if dir[0] in valid and dir[1] in valid:
            newLoc =  (self._playerLoc[0] + dir[0], self._playerLoc[1] + dir[1])

            # if the new location is in bounds move player and return true
            if self._neighborhood.inBounds(newLoc):
                self._playerLoc = newLoc
                return True
        # otherwise return false
        return False

    def attackHouse(self, loc, weaponNum):
        """
        helper function that tells the player to attack all the monsters in a
        house

        :param loc: houses position in tuple
        :param weaponNum: weapon id to use
        """

        # if game is over return
        if not self._isPlaying:
            return

        # give the player the monsters from the house to attack
        self._player.attackAll(self._neighborhood.getHouse(loc), weaponNum)
        # tell the monsters in the house to attack the player back
        self._neighborhood.getHouse(loc).dealDamage(self._player)

        if self.getNeighborhood().isClear():
            self._isPlaying = False
