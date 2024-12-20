### AI Generated Content ###

import pathlib
import re

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        list: Lines from the input file
    """
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def solve_part1(input_data):
    """
    Find all valid mul(X,Y) instructions and sum their products.
    
    Args:
        input_data (list): Lines of corrupted memory
    
    Returns:
        int: Sum of all multiplication results
    """
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total_sum = 0
    
    for line in input_data:
        matches = re.finditer(pattern, line)
        for match in matches:
            x = int(match.group(1))
            y = int(match.group(2))
            total_sum += x * y
            
    return total_sum

def solve_part2(input_data):
    """
    Find all valid mul(X,Y) instructions and sum their products,
    taking into account do() and don't() instructions.
    
    Args:
        input_data (list): Lines of corrupted memory
    
    Returns:
        int: Sum of all enabled multiplication results
    """
    # Patterns for different instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    total_sum = 0
    
    for line in input_data:
        # Find all instructions with their positions
        instructions = []
        
        # Find multiplication instructions
        for match in re.finditer(mul_pattern, line):
            instructions.append({
                'type': 'mul',
                'pos': match.start(),
                'x': int(match.group(1)),
                'y': int(match.group(2))
            })
        
        # Find do() instructions
        for match in re.finditer(do_pattern, line):
            instructions.append({
                'type': 'do',
                'pos': match.start()
            })
            
        # Find don't() instructions
        for match in re.finditer(dont_pattern, line):
            instructions.append({
                'type': 'dont',
                'pos': match.start()
            })
        
        # Sort instructions by position
        instructions.sort(key=lambda x: x['pos'])
        
        # Process instructions in order
        enabled = True  # Multiplications are enabled by default
        
        for instruction in instructions:
            if instruction['type'] == 'do':
                enabled = True
            elif instruction['type'] == 'dont':
                enabled = False
            elif instruction['type'] == 'mul' and enabled:
                total_sum += instruction['x'] * instruction['y']
    
    return total_sum

def main():
    # Get day number from filename
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