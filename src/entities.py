class Entity:
    def __init__(self, name):
        self.name = name

class Player(Entity):
    def __init__(self, name, health):
        super().__init__(name)
        self.health = health

class Enemy(Entity):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.attack_power = attack_power
