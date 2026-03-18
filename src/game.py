class Game:
    def __init__(self):
        self.running = True

    def start(self):
        while self.running:
            self.update()
            self.render()

    def update(self):
        pass  # Logic to update the game state

    def render(self):
        pass  # Logic to render the game state

    def stop(self):
        self.running = False
