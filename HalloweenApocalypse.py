from Game import Game

game = Game()

while True:
    print("what house would you like to attack: \n")
    hx = int(input("x: \n"))
    hy = int(input("y: \n"))
    print("choose weapon: \n")
    game.player.printWeapons()
    wNum = int(input("Choice: \n"))
    game.neighborhood.attack(game.player, hx, hy)
