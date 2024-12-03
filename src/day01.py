import pathlib

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        tuple: Two lists of integers
    """
    # Construct the path to the input file
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'
    
    # Read the input, split into left and right lists
    with open(input_path, 'r') as f:
        # Assume input is pairs of numbers, one pair per line
        left_list = []
        right_list = []
        
        for line in f:
            # Split the line into two numbers
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

def solve_part1(input_data):
    """
    Solve Part 1 of the puzzle.
    
    Args:
        input_data (tuple): Tuple of two lists of integers
    
    Returns:
        int: Total distance between paired sorted lists
    """
    # Unpack the input data
    left_list, right_list = input_data
    
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate total distance
    total_distance = sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))
    
    return total_distance

def solve_part2(input_data):
    """
    Solve Part 2 of the puzzle (placeholder).
    
    Args:
        input_data (tuple): Tuple of two lists of integers
    
    Returns:
        Result of Part 2 solution
    """
    # Placeholder for Part 2
    return None

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
    if part2_solution is not None:
        print(f"Day {day_number} - Part 2 Solution: {part2_solution}")

if __name__ == '__main__':
    main()