import random

class Dungeon:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dungeon = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]

    def generate(self):
        self._recursive_backtracking(1, 1)

    def _recursive_backtracking(self, x, y):
        # Directions: right, down, left, up
        directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 < nx < self.width) and (0 < ny < self.height) and not self.visited[ny][nx]:
                self.dungeon[y + dy // 2][x + dx // 2] = ' '
                self.dungeon[ny][nx] = ' '
                self.visited[ny][nx] = True
                self._recursive_backtracking(nx, ny)

    def display(self):
        for row in self.dungeon:
            print(''.join(row))

# Example usage:
if __name__ == '__main__':
    dungeon = Dungeon(21, 21)
    dungeon.generate()
    dungeon.display()