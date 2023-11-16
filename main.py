import read_input, MarsRover


grid, obstacles, command_series_list = read_input.read_input_file("input.txt")
initial_position = (0, 0,'N')
 # Initialize the Mars Rover with the initial position or (0, 0, 'N') for the first iteration
rover = MarsRover.MarsRover(grid, obstacles) 

for command_series in command_series_list:
    # Split the command series into individual characters
    commands_list = [char for char in command_series]
        
    if initial_position:
        rover.x, rover.y, rover.direction = initial_position
       
    rover.execute_commands(commands_list)
    position = rover.print_current_position()
    # Save the position for the next iteration
    initial_position = (rover.x, rover.y, rover.direction)
