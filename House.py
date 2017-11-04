from Entities import Monsters
from random import randint

class House(object):
    def __init__(self):
        self.monsters = House.generateMonsters()

    def generateMonsters():
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(Monsters.generateRandomMonster())
        return monsterList
