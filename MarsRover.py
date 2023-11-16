class MarsRover:
    # defining class variables
    def __init__(self, grid, obstacles):
        self.grid = grid
        self.updated_grid = tuple(x - 1 for x in grid)
        self.obstacles = obstacles
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.obstacle_encountered = False

    # defining rotate left function based on different directions
    def rotate_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'W':
            self.direction = 'S'

    # defining rotate right function based on different directions
    def rotate_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    # defining move forward function
    def move_forward(self):
        new_x, new_y = self.x, self.y
        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'W':
            new_x -= 1

        if self.is_obstacle(new_x, new_y):
            return self.obstacle_encountered

        if self.is_not_valid(new_x, new_y):
            x_max, y_max = self.updated_grid
            if new_x < 0:
                new_x = x_max
            elif new_x > x_max:
                new_x = 0
            if new_y < 0:
                new_y = y_max
            elif new_y > y_max:
                new_y = 0

        self.x, self.y = new_x, new_y
    
    # defining move backward function
    def move_backward(self):
        new_x, new_y = self.x, self.y
        if self.direction == 'N':
            new_y -= 1
        elif self.direction == 'E':
            new_x -= 1
        elif self.direction == 'S':
            new_y += 1
        elif self.direction == 'W':
            new_x += 1

        if self.is_obstacle(new_x, new_y):
            return self.obstacle_encountered

        if self.is_not_valid(new_x, new_y):
            x_max, y_max = self.updated_grid
            if new_x < 0:
                new_x = x_max
            elif new_x > x_max:
                new_x = 0
            if new_y < 0:
                new_y = y_max
            elif new_y > y_max:
                new_y = 0

        self.x, self.y = new_x, new_y

    # to check if the next position is an obstacle
    def is_obstacle(self, x, y):
        if (x, y) in self.obstacles:
            self.obstacle_encountered = True
        else:
            self.obstacle_encountered = False
        return self.obstacle_encountered

    # to check if the next move is valid (if the rover reaches grid borders)
    def is_not_valid(self, x, y):
        x_max, y_max = self.updated_grid 
        if x < 0:
            self.x = x_max
        elif x > x_max:
            self.x = 0
        if y < 0:
            self.y = y_max
        elif y > y_max:
            self.y = 0
        return True
    
    # defining commands function 
    def execute_commands(self, commands):
        for command in commands:
            if command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()
            elif command == 'F':
                self.move_forward()
            elif command == 'B':
                self.move_backward()

    # printing the current position 
    def get_position(self):
        if self.obstacle_encountered:
            print(f'O:{self.x}:{self.y}:{self.direction}')
        else:
            print(f'{self.x}:{self.y}:{self.direction}')
