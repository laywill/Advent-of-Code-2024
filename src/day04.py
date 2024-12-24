### AI Generated Content ###

import pathlib

def read_input(day_number):
    """Read input from a text file."""
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def check_direction(grid, row, col, dr, dc, target="XMAS"):
    """Check if target string exists starting from a position in a given direction."""
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

def get_diagonal_string(grid, row, col, dr, dc):
    """
    Get a 3-letter string along a diagonal direction.
    
    Args:
        grid (list): The word search grid
        row (int): Starting row
        col (int): Starting column
        dr (int): Row direction (-1 or 1)
        dc (int): Column direction (-1 or 1)
    
    Returns:
        str: The 3-letter string found along the diagonal, or None if out of bounds
    """
    # Check if we can get a 3-letter string in this direction
    if (row + 2*dr < 0 or row + 2*dr >= len(grid) or 
        col + 2*dc < 0 or col + 2*dc >= len(grid[0])):
        return None
    
    # Build the 3-letter string
    return (grid[row][col] + 
            grid[row + dr][col + dc] + 
            grid[row + 2*dr][col + 2*dc])

def check_x_mas(grid, center_row, center_col):
    """
    Check if there's a valid X-MAS pattern centered at the given position.
    A valid pattern requires finding "MAS" or "SAM" on both diagonals through the center point.
    """
    valid_strings = {"MAS", "SAM"}
    
    # Define the diagonal directions
    diagonal_pairs = [
        # Each tuple contains (dr1, dc1, dr2, dc2) for the two parts of a diagonal
        ((-1, -1), (1, 1)),    # Top-left to bottom-right diagonal
        ((-1, 1), (1, -1))     # Top-right to bottom-left diagonal
    ]
    
    # For each diagonal, collect all possible strings in both directions
    diagonal1_strings = []
    diagonal2_strings = []
    
    # Check first diagonal (top-left to bottom-right)
    for dr, dc in diagonal_pairs[0]:
        string = get_diagonal_string(grid, center_row, center_col, dr, dc)
        if string:
            diagonal1_strings.append(string)
            
    # Check second diagonal (top-right to bottom-left)
    for dr, dc in diagonal_pairs[1]:
        string = get_diagonal_string(grid, center_row, center_col, dr, dc)
        if string:
            diagonal2_strings.append(string)
    
    # We need at least one valid string on each diagonal
    has_valid_diagonal1 = any(s in valid_strings for s in diagonal1_strings)
    has_valid_diagonal2 = any(s in valid_strings for s in diagonal2_strings)
    
    return has_valid_diagonal1 and has_valid_diagonal2

def solve_part1(input_data):
    """Solve Part 1: Find all instances of XMAS in any direction."""
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
    
    for row in range(height):
        for col in range(width):
            for dr, dc in directions:
                if check_direction(grid, row, col, dr, dc):
                    count += 1
    
    return count

def solve_part2(input_data):
    """Solve Part 2: Find all X-MAS patterns where both diagonals contain MAS/SAM."""
    grid = input_data
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # Check every possible center position for an X pattern
    # We need at least 2 spaces in all directions for a complete X-MAS
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if check_x_mas(grid, row, col):
                count += 1
    
    return count

def main():
    day_number = int(pathlib.Path(__file__).stem[3:])
    input_data = read_input(day_number)
    
    part1_solution = solve_part1(input_data)
    print(f"Day {day_number} - Part 1 Solution: {part1_solution}")
    
    part2_solution = solve_part2(input_data)
    print(f"Day {day_number} - Part 2 Solution: {part2_solution}")

if __name__ == '__main__':
    main()