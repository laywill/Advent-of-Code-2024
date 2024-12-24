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
    print(f"\nChecking direction from ({row},{col}) with direction ({dr},{dc}) for target '{target}'")
    
    # Check boundaries
    if (row + dr * (len(target) - 1) < 0 or 
        row + dr * (len(target) - 1) >= len(grid) or
        col + dc * (len(target) - 1) < 0 or 
        col + dc * (len(target) - 1) >= len(grid[0])):
        print(f"  Out of bounds: would end at ({row + dr * (len(target) - 1)},{col + dc * (len(target) - 1)})")
        return False
    
    # Build the word
    word = ""
    for i in range(len(target)):
        current_row = row + dr * i
        current_col = col + dc * i
        word += grid[current_row][current_col]
        print(f"  Position ({current_row},{current_col}): added '{grid[current_row][current_col]}' -> word so far: '{word}'")
    
    match = word == target
    print(f"  Found word: '{word}' -> {'matches' if match else 'does not match'} target '{target}'")
    return match

def get_diagonal_string(grid, row, col, dr, dc):
    """Get a 3-letter string along a diagonal direction."""
    print(f"\nTrying diagonal from ({row},{col}) with direction ({dr},{dc})")
    
    # Check if we can get a 3-letter string in this direction
    if (row + 2*dr < 0 or row + 2*dr >= len(grid) or 
        col + 2*dc < 0 or col + 2*dc >= len(grid[0])):
        print(f"  Out of bounds at ({row + 2*dr},{col + 2*dc})")
        return None
    
    # Build the 3-letter string
    string = (grid[row][col] + 
            grid[row + dr][col + dc] + 
            grid[row + 2*dr][col + 2*dc])
    print(f"  Found string: {string}")
    return string

def check_x_mas(grid, center_row, center_col):
    """Check for valid X-MAS pattern centered at the given position."""
    print(f"\nChecking center position ({center_row},{center_col})")
    print(f"Grid size: {len(grid)}x{len(grid[0])}")
    print("Current grid state:")
    for i, row in enumerate(grid):
        print(f"Row {i}: {row}")
    
    valid_strings = {"MAS", "SAM"}
    
    # Define the diagonal directions
    diagonal_pairs = [
        ((-1, -1), (1, 1)),    # Top-left to bottom-right diagonal
        ((-1, 1), (1, -1))     # Top-right to bottom-left diagonal
    ]
    
    print("\nChecking first diagonal (top-left to bottom-right):")
    diagonal1_strings = []
    for dr, dc in diagonal_pairs[0]:
        string = get_diagonal_string(grid, center_row, center_col, dr, dc)
        if string:
            diagonal1_strings.append(string)
    print(f"Found strings on diagonal 1: {diagonal1_strings}")
    
    print("\nChecking second diagonal (top-right to bottom-left):")
    diagonal2_strings = []
    for dr, dc in diagonal_pairs[1]:
        string = get_diagonal_string(grid, center_row, center_col, dr, dc)
        if string:
            diagonal2_strings.append(string)
    print(f"Found strings on diagonal 2: {diagonal2_strings}")
    
    # Check for valid strings on each diagonal
    has_valid_diagonal1 = any(s in valid_strings for s in diagonal1_strings)
    has_valid_diagonal2 = any(s in valid_strings for s in diagonal2_strings)
    
    print(f"\nValid strings found:")
    print(f"  Diagonal 1: {has_valid_diagonal1}")
    print(f"  Diagonal 2: {has_valid_diagonal2}")
    
    return has_valid_diagonal1 and has_valid_diagonal2

def solve_part1(input_data):
    """Solve Part 1: Find all instances of XMAS in any direction."""
    print("\nSolving Part 1")
    print("Input grid:")
    for row in input_data:
        print(row)
    
    grid = input_data
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    print(f"\nChecking grid positions (height={height}, width={width})")
    for row in range(height):
        for col in range(width):
            print(f"\n=== Checking position ({row},{col}) ===")
            for dr, dc in directions:
                if check_direction(grid, row, col, dr, dc, "XMAS"):
                    print(f"Found XMAS at ({row},{col}) in direction ({dr},{dc})")
                    count += 1
    
    print(f"\nTotal XMAS patterns found: {count}")
    return count

def solve_part2(input_data):
    """Solve Part 2: Find all X-MAS patterns where both diagonals contain MAS/SAM."""
    print("\nSolving Part 2")
    print("Input grid:")
    for row in input_data:
        print(row)
    
    grid = input_data
    height = len(grid)
    width = len(grid[0])
    count = 0
    
    # We need at least 2 spaces in all directions for a complete X-MAS
    print(f"\nChecking grid positions (height={height}, width={width})")
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            print(f"\n=== Checking position ({row},{col}) ===")
            if check_x_mas(grid, row, col):
                print(f"Found valid X-MAS pattern at ({row},{col})")
                count += 1
    
    print(f"\nTotal X-MAS patterns found: {count}")
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