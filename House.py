from Entities import Monsters
from random import randint
from Observers.Observer import Observer

class House(Observer):
    def __init__(self):
        self._monsters = self.generateMonsters()

    def __str__(self):
        s = "House Contains: \n"
        for mon in self._monsters:
            s.append("{} \n".format(mon))
        return s

    def getMonsterlist(self):
        return self._monsters

    def receiveUpdate(self, info):
        if info in self._monsters:
            self._monsters[self._monsters.index(info)] = Monsters.Person()

    def attackAll(self, player, weapon):
        for mon in self._monsters:
            player.dealDamage(mon, weapon)

    def dealDamage(self, player):
        for mon in self._monsters:
            if not player.isDead():
                mon.dealDamage(player)

    # TODO add generateMonstersList
    def generateMonsters(self):
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(Monsters.generateRandomMonster())
            monsterList[len(monsterList) - 1].add_observer(self)
        return monsterList
