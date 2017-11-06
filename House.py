from Entities import Monsters
from random import randint

class House(object):
    def __init__(self):
        self._monsters = House.generateMonsters()

    def takeDamage(self, amount, weapon):
        for mon in _monsters:
            mon.takeDamage(amount, weapon)

    def dealDamage(self, player):
        for Mon in _monsters:
            mon.dealDamage(player)

    def generateMonsters():
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(Monsters.generateRandomMonster())
        return monsterList
