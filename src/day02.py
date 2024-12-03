import pathlib

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        list: List of lists of integers (reports)
    """
    # Construct the path to the input file
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'
    
    # Read the input, convert each line to list of integers
    with open(input_path, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]

def is_safe_without_one_level(report):
    """
    Check if a report is safe, allowing removal of one level.
    
    A report is safe if:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    
    Args:
        report (list): List of integer levels
    
    Returns:
        bool: True if the report is safe, False otherwise
    """
    # First check if it's already safe without removing anything
    if is_safe_report(report):
        return True
    
    # Try removing each level and check if the resulting list is safe
    for i in range(len(report)):
        # Create a new list without the i-th element
        reduced_report = report[:i] + report[i+1:]
        
        if is_safe_report(reduced_report):
            return True
    
    return False

def is_safe_report(report):
    """
    Check if a report is safe without removing levels.
    
    Args:
        report (list): List of integer levels
    
    Returns:
        bool: True if the report is safe, False otherwise
    """
    # Check if all increasing
    increasing = all(report[i+1] - report[i] >= 1 and report[i+1] - report[i] <= 3 
                     for i in range(len(report) - 1))
    
    # Check if all decreasing
    decreasing = all(report[i] - report[i+1] >= 1 and report[i] - report[i+1] <= 3 
                     for i in range(len(report) - 1))
    
    return increasing or decreasing

def solve_part1(input_data):
    """
    Solve Part 1 of the puzzle.
    
    Args:
        input_data (list): List of reports (each report is a list of integers)
    
    Returns:
        int: Number of safe reports
    """
    # Count safe reports without Problem Dampener
    return sum(1 for report in input_data if is_safe_report(report))

def solve_part2(input_data):
    """
    Solve Part 2 of the puzzle with Problem Dampener.
    
    Args:
        input_data (list): List of reports (each report is a list of integers)
    
    Returns:
        int: Number of safe reports with Problem Dampener
    """
    # Count safe reports with Problem Dampener
    return sum(1 for report in input_data if is_safe_without_one_level(report))

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