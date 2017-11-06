from .Entity import Entity

class Player(Entity):

    def dealDamage(self, house, weapon):
        house.takeDamage(self.attack)
