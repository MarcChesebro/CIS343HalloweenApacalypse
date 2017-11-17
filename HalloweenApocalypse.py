#!/usr/bin/env python3

from Game import Game

if __name__ == "__main__":

    commands = ["m", "a", "p", "q"]

    print("Everyone in The neighborhood has been turned into monsters due to tainted candy. clear all the houses of the monsters to win")
    name = input("whats your Name: ")
    game = Game(playerName=name)

    while True:
        if not game.getStatus():
            break

        print("location: {}".format(game.getPlayerLoc()))
        command = input("Enter m, a, p, or q: m to move, a to attack, p to peek into the house, and q to quit\n")
        if command in commands:
            if command is commands[0]:
                print("pick move dir: ")
                try:
                    x = int(input("x: "))
                    y = int(input("y: "))
                except ValueError:
                    print("not a valid number")
                else:
                    if not game.move((x, y)):
                        print("invalid move")

            if command is commands[1]:
                print("choose weapon: \n")
                game.getPlayer().printWeapons()

                try:
                    choice = int(input("choose: "))
                except ValueError:
                    print("not a valid number")
                else:

                    game.attackHouse(game.getPlayerLoc(), choice)

            if command is commands[2]:
                game.getNeighborhood().peekHouse(game.getPlayerLoc())
            if command is commands[3]:
                print("thanks for playing!")
                exit()

        else:
            print("invalid command")
    print("you lost!")
