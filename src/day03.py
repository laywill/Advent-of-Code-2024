### AI Generated Content ###

import pathlib
import re

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        list: Lines from the input file, or processed input as needed
    """
    # Construct the path to the input file
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        return f.read().strip()

def solve_part1(input_data):
    """
    Solve Part 1 of the puzzle by finding and summing valid mul instructions.
    
    Args:
        input_data (str): Corrupted memory string
    
    Returns:
        int: Sum of multiplication results from valid mul instructions
    """
    # Regex to match valid mul instructions
    # Looks for mul(X,Y) where X and Y are 1-3 digit numbers
    # Allows for some whitespace, ignores invalid characters
    mul_pattern = r'mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    
    # Find all valid mul instructions and multiply their numbers
    results = []
    for match in re.finditer(mul_pattern, input_data):
        x = int(match.group(1))
        y = int(match.group(2))
        results.append(x * y)
    
    # Return the sum of multiplication results
    return sum(results)

def solve_part2(input_data):
    """
    Solve Part 2 of the puzzle with do() and don't() instructions.
    
    Args:
        input_data (str): Corrupted memory string
    
    Returns:
        int: Sum of multiplication results from enabled mul instructions
    """
    # Regex patterns
    mul_pattern = r'mul\s*\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)'
    do_pattern = r'do\s*\(\s*\)'
    dont_pattern = r'don\'?t\s*\(\s*\)'
    
    # Track mul instruction state
    mul_enabled = True
    results = []
    
    # Scan through the input tracking state changes and mul instructions
    pos = 0
    while pos < len(input_data):
        # Check for do() instruction
        do_match = re.search(do_pattern, input_data[pos:])
        if do_match:
            mul_enabled = True
            pos += do_match.end()
            continue
        
        # Check for don't() instruction
        dont_match = re.search(dont_pattern, input_data[pos:])
        if dont_match:
            mul_enabled = False
            pos += dont_match.end()
            continue
        
        # Check for mul instruction
        mul_match = re.search(mul_pattern, input_data[pos:])
        if mul_match:
            if mul_enabled:
                x = int(mul_match.group(1))
                y = int(mul_match.group(2))
                results.append(x * y)
            pos += mul_match.end()
            continue
        
        # Move forward if no match found
        pos += 1
    
    # Return the sum of multiplication results
    return sum(results)

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