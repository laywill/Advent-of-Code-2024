import os
import sys

def create_input_file(day_number):
    """
    Create an empty input file for a specific day.
    
    Args:
        day_number (int): Day number (1-25)
    """
    inputs_dir = os.path.join(os.path.dirname(__file__), '..', 'inputs')
    os.makedirs(inputs_dir, exist_ok=True)
    
    filename = os.path.join(inputs_dir, f'day{day_number:02d}.txt')
    
    if os.path.exists(filename):
        print(f"Input file for Day {day_number} already exists.")
        return
    
    # Create an empty file
    with open(filename, 'w') as f:
        pass
    
    print(f"Created empty input file: {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python setup_input.py <day_number>")
        sys.exit(1)
    
    try:
        day = int(sys.argv[1])
        if not 1 <= day <= 25:
            raise ValueError("Day must be between 1 and 25")
        
        create_input_file(day)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()