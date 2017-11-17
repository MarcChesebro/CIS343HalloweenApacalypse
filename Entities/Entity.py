from Observers.Observable import Observable

class Entity(Observable):
    """
    Base class for all Entities in the game
    (anything that has health and takes/deals damage)
    """
    def __init__(self, health = 100, attack = 10):
        """
        simple constructor with default values

        :param health: totalhealth of the monster
        :param attack: base attack of the monster
        """
        #set instance varables
        self._health = health
        self._attack = attack
        # call Observavle constructor
        super(Entity, self).__init__()

    def sendUpdate(self):
        """
        overload sendUpdate function from the Observable class.
        send self when we die so the Observer can update its variables
        """
        super(Entity, self).sendUpdate(info=self)

    def isDead(self):
        """
        function that retruns True if this Entity is dead or False if it is not
        """
        if self._health <= 0:
            return True
        return False

    def takeDamage(self, amount):
        """
        a function for taking damage. remove that amount of health then if
        the Entity dies sendUpdate to Observers

        :param amount: amount of damage to take
        """
        #reduce health
        self._health = self._health - amount

        if self._health < 0:
            self._health = 0

        self.printDamage(amount)

        #if the entity is dead update observers
        if self.isDead():
            self.sendUpdate()
            self.remove_all_observers()

    def printDamage(self, amount):
        """
        prints the damage to the console in a nice away

        :param amount: amount of damage to print to the screen
        """
        if not self.isDead():
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
        else:
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
            print("{} is defeated and transforms back into a human!".format(self))

    def dealDamage(self, target, modifier=1):
        """
        a function for dealing damage to another entitiy

        :param target: Entity to deal damage to
        :param modifier: damage multiplier
        """
        target.takeDamage(self._attack * modifier)
