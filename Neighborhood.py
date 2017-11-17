from House import House

class Neighborhood(object):
    """
    Neighborhood class that hold a 2D array of Houses and provides functionality
    for the player to interact with them
    """
    def __init__(self, height=5, width=5):
        """
        Constructor to initialize the list of Houses

        :param height: height of the Houses array
        :param width: width of the House array
        """

        # generate 2D array of houses. Houses will populate themselves
        self._houses = [[House() for x in range(width)] for y in range(height)]

    def getHouse(self, loc):
        """
        returns the house at the loc

        :param loc: tuple holding location of the house
        :return: house at loc
        """
        return self._houses[loc[0]][loc[1]]

    def peekHouse(self, loc):
        """
        peeks into a house displaying all the monsters inside of it

        :param loc: tuple(x, y) of the house to peek into
        """

        # check that the loc is in bounds
        if self.inBounds(loc):

            return print(self._houses[loc[0]][loc[1]])
        else:
            return "invalid location!"

    def inBounds(self, loc):
        """
        checks if a location is in range of the Houses

        :param loc: loc to check
        :return: return true if the loc is in bounds or false otherwise
        """
        if loc[0] in range(0, len(self._houses)) and loc[1] in range(0, len(self._houses[0])):
            return True
        else:
            return False
