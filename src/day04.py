### AI Generated Content ###

import pathlib

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        list: Lines from the input file as a list of strings
    """
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def check_direction(grid, row, col, dr, dc, target="XMAS"):
    """
    Check if the target word exists starting from a position in a given direction.
    
    Args:
        grid (list): The word search grid
        row (int): Starting row
        col (int): Starting column
        dr (int): Row direction (-1, 0, or 1)
        dc (int): Column direction (-1, 0, or 1)
        target (str): The word to find (default: "XMAS")
    
    Returns:
        bool: True if the word is found in this direction, False otherwise
    """
    if (
        row + dr * (len(target) - 1) < 0 
        or row + dr * (len(target) - 1) >= len(grid)
        or col + dc * (len(target) - 1) < 0 
        or col + dc * (len(target) - 1) >= len(grid[0])
    ):
        return False
    
    for i in range(len(target)):
        if grid[row + dr * i][col + dc * i] != target[i]:
            return False
    return True

def check_mas_direction(grid, row, col, dr, dc):
    """
    Check if "MAS" exists starting from a position in a given direction.
    Also checks for "SAM" in the same direction.
    
    Args:
        grid (list): The word search grid
        row (int): Starting row
        col (int): Starting column
        dr (int): Row direction (-1, 0, or 1)
        dc (int): Column direction (-1, 0, or 1)
    
    Returns:
        bool: True if either "MAS" or "SAM" is found in this direction
    """
    return check_direction(grid, row, col, dr, dc, "MAS") or check_direction(grid, row, col, dr, dc, "SAM")

def check_x_mas(grid, center_row, center_col):
    """
    Check if there's a valid X-MAS pattern centered at the given position.
    An X-MAS pattern consists of two "MAS" strings (or "SAM") in opposite directions.
    
    Args:
        grid (list): The word search grid
        center_row (int): Row of the center of the X
        center_col (int): Column of the center of the X
    
    Returns:
        bool: True if a valid X-MAS pattern is found
    """
    # Define the four cardinal direction pairs (each pair represents opposite directions)
    direction_pairs = [
        # Vertical: top and bottom
        ((-1, 0), (1, 0)),
        # Horizontal: left and right
        ((0, -1), (0, 1)),
    ]
    
    for (dr1, dc1), (dr2, dc2) in direction_pairs:
        # Check both directions from the center
        if check_mas_direction(grid, center_row, center_col, dr1, dc1) and \
           check_mas_direction(grid, center_row, center_col, dr2, dc2):
            return True
    
    return False

def solve_part1(input_data):
    """
    Solve Part 1 of the puzzle.
    
    Args:
        input_data (list): List of strings representing the word search grid
    
    Returns:
        int: Total number of times XMAS appears in the grid
    """
    grid = input_data
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # Define all eight directions
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
        (0, -1),           (0, 1),    # Left, Right
        (1, -1),  (1, 0),  (1, 1)     # Down-left, Down, Down-right
    ]
    
    # Check every starting position
    for row in range(height):
        for col in range(width):
            # Check all eight directions from this position
            for dr, dc in directions:
                if check_direction(grid, row, col, dr, dc):
                    count += 1
    
    return count

def solve_part2(input_data):
    """
    Solve Part 2 of the puzzle.
    
    Args:
        input_data (list): List of strings representing the word search grid
    
    Returns:
        int: Total number of X-MAS patterns found
    """
    grid = input_data
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # Check every possible center position for an X pattern
    # We need at least 2 spaces in each direction for a complete X-MAS
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if check_x_mas(grid, row, col):
                count += 1
    
    return count

def main():
    # Automatically extract day number from filename
    day_number = int(pathlib.Path(__file__).stem[3:])

    # Read input
    input_data = read_input(day_number)

    # Solve Part 1
    part1_solution = solve_part1(input_data)
    print(f"Day {day_number} - Part 1 Solution: {part1_solution}")

    # Solve Part 2
    part2_solution = solve_part2(input_data)
    print(f"Day {day_number} - Part 2 Solution: {part2_solution}")

if __name__ == '__main__':
    main()