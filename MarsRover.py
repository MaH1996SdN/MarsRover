class MarsRover:
    def __init__(self, grid, obstacles):
        self.grid = grid
        self.obstacles = obstacles
        self.x = 0
        self.y = 0
        self.direction = 'N'