from Entities import Monsters
from random import randint
from Observers.Observer import Observer

class House(Observer):
    def __init__(self):
        self._monsters = self.generateMonsters()

    def __str__(self):
        """
        returns a string to represent the object
        """
        s = "\nHouse Contains: \n"
        if len(self._monsters) == 0:
            s = s + "Empty\n"
        for mon in self._monsters:
            s = s + "{} \n".format(mon)

        return s

    def getMonsterlist(self):
        """
        return the monster list

        :return: the monsters list
        """
        return self._monsters

    def isClear(self):
        """
        a function that tells if the house only has humans left in it

        :retrun: true if the house only contains humans False otherwise
        """
        for mon in self._monsters:
            if not(type(mon) is Monsters.Person):
                return False
        return True

    def receiveUpdate(self, info):
        """
        overriding recieveUpdate from the Observer class.
        if we recieve an update check if it is a monster in our monster list
        if it is remove it from the monster list as it has modified

        :param info: monster to remove
        """
        if info in self._monsters:
            self._monsters[self._monsters.index(info)] = Monsters.Person()

    def dealDamage(self, player):
        """
        have the monsters in the house attack a target

        :param player: player to have the monsters attack
        """
        for mon in self._monsters:
            # make sure the player is alive before attacking
            if not player.isDead():
                mon.dealDamage(player)

    def generateMonsters(self):
        """
        generate a starting list of monsters using helper functions from then
        Monsters.py
        """
        # instantiate empty list
        monsterList = []

        # generate 0-10 monsters
        for i in range(0, randint(0, 10)):
            #add monster to end of list
            monsterList.append(Monsters.generateRandomMonster())
            # add house to the monsters observer list
            monsterList[len(monsterList) - 1].add_observer(self)
        #return the monster list
        return monsterList
