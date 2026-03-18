class Menu:
    def __init__(self):
        self.options = ["Start Game", "Options", "Quit"]

    def display(self):
        print("Menu:")
        for index, option in enumerate(self.options):
            print(f"{index + 1}. {option}")

class HUD:
    def __init__(self):
        self.health = 100
        self.score = 0

    def render(self):
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")

if __name__ == '__main__':
    menu = Menu()
    menu.display()
    hud = HUD()
    hud.render()