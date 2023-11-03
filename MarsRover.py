class MarsRover:
    def __init__(self, grid, obstacles):
        self.grid = grid
        self.obstacles = obstacles
        self.x = 0
        self.y = 0
        self.direction = 'N'

    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'

    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'


# defining function for reading input file and initializing grid, obstacles and commmands

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.read()

        # reading grid size and store it in a tuple
        grid_line = next(line for line in lines if line.startswith("Size"))
        grid = tuple(int(word) for word in grid_line.split()[1:])

        # reading obstacles and store them in a list
        obstacles = [(int(line.split()[1]), int(line.split()[2])) for line in lines if line.startswith("Obstacle")]
