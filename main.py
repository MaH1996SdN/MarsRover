import read_input, MarsRover


grid, obstacles, command_series_list = read_input.read_input_file("input.txt")
initial_position = (0, 0,'N')
 # Initialize the Mars Rover with the initial position or (0, 0, 'N') for the first iteration
rover = MarsRover.MarsRover(grid, obstacles, initial_position) 

for command_series in command_series_list:
    # Split the command series into individual characters
    commands_list = [char for char in command_series]   
    rover.execute_commands(commands_list)
    rover.print_current_position()
