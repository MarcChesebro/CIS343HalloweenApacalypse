from Entities import Monsters
from random import randint
from Observers.Observer import Observer

class House(Observer):
    def __init__(self):
        self._monsters = House.generateMonsters()

    def update(self):
        print("house was updated")

    def takeDamage(self, amount, weapon):
        for i, mon in enumerate(self._monsters):
            mon.takeDamage(amount, weapon)
            if mon.isDead:
                self._monsters[i] = Monsters.Person()

    def dealDamage(self, player):
        for Mon in _monsters:
            mon.dealDamage(player)

    def generateMonsters():
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(Monsters.generateRandomMonster())
        return monsterList
