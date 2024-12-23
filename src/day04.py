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
    
    word = ""
    for i in range(len(target)):
        word += grid[row + dr * i][col + dc * i]
    return word == target

def check_x_mas(grid, center_row, center_col):
    """
    Check if there's a valid X-MAS pattern centered at the given position.
    A valid pattern requires finding "MAS" or "SAM" on both diagonals through the center point.
    
    Args:
        grid (list): The word search grid
        center_row (int): Row of the center of the X
        center_col (int): Column of the center of the X
    
    Returns:
        bool: True if a valid X-MAS pattern is found
    """
    # Get the strings along both diagonals from the center point
    def get_diagonal_strings(row, col):
        """Helper function to get all possible 3-letter strings along a diagonal"""
        strings = []
        # Try both directions from the center for the diagonal
        for dr, dc in [(1, 1), (-1, -1)]:  # One diagonal
            if (row + 2*dr >= 0 and row + 2*dr < len(grid) and 
                col + 2*dc >= 0 and col + 2*dc < len(grid[0])):
                word = (grid[row][col] + 
                       grid[row + dr][col + dc] + 
                       grid[row + 2*dr][col + 2*dc])
                strings.append(word)
        return strings

    def get_other_diagonal_strings(row, col):
        """Helper function to get all possible 3-letter strings along the other diagonal"""
        strings = []
        # Try both directions from the center for the other diagonal
        for dr, dc in [(1, -1), (-1, 1)]:  # Other diagonal
            if (row + 2*dr >= 0 and row + 2*dr < len(grid) and 
                col + 2*dc >= 0 and col + 2*dc < len(grid[0])):
                word = (grid[row][col] + 
                       grid[row + dr][col + dc] + 
                       grid[row + 2*dr][col + 2*dc])
                strings.append(word)
        return strings

    # Get all possible strings on both diagonals
    diag1_strings = get_diagonal_strings(center_row, center_col)
    diag2_strings = get_other_diagonal_strings(center_row, center_col)

    # Check if we can find MAS or SAM on both diagonals
    valid_strings = {"MAS", "SAM"}
    return (any(s in valid_strings for s in diag1_strings) and 
            any(s in valid_strings for s in diag2_strings))

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