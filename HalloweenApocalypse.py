#!/usr/bin/env python3

from Game import Game

game = Game()
commands = ["m", "a", "p"]

if __name__ == "__main__":

    while True:
        if not game.getStatus():
            break

        print("location: {}".format(game.getPlayerLoc()))
        command = input("Enter m, a, or p: m to move, a to attack, and p to peek into the house\n")
        if command in commands:
            if command is commands[0]:
                print("pick move dir: ")
                x = int(input("x: "))
                y = int(input("y: "))
                if not game.move((x, y)):
                    print("invalid move")

            if command is commands[1]:
                print("choose weapon: \n")
                game.getPlayer().printWeapons()

                game.attackHouse(game.getPlayerLoc(), int(input("choose: ")))

            if command is commands[2]:
                game.getNeighborhood().peekHouse(game.getPlayerLoc())

        else:
            print("invalid command")
    print("you lost!")
