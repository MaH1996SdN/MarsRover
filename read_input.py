# defining function for reading input file and initializing grid, obstacles and commmands

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

        # reading grid size and store it in a tuple
        grid_line = next(line for line in lines if line.startswith("Size"))
        grid = tuple(int(word) for word in grid_line.split()[1:])

        # reading obstacles and store them in a list
        obstacles = [(int(line.split()[1]), int(line.split()[2])) for line in lines if line.startswith("Obstacle")]

        commands_lines = []
        recording_commands = False
        
        for line in lines:
            line = line.strip()
            if recording_commands:
                if line:
                    commands_lines.append(line)
                else:
                    recording_commands = False
            elif line.startswith("Commands"):
                recording_commands = True
        
        # Split each command series into individual characters
        command_series_list = [line for line in commands_lines]   
        return grid, obstacles, command_series_list
    
