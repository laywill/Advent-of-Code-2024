### AI Generated Content ###

import pathlib
from typing import List, Dict, Set, Tuple
from collections import defaultdict, deque

def read_input(day_number: int) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """
    Read input from a text file and parse into rules and updates.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        Tuple containing:
        - List of tuples (before, after) representing ordering rules
        - List of lists containing the page numbers for each update
    """
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Find the empty line that separates rules from updates
    separator_idx = lines.index('')
    
    # Parse rules
    rules = []
    for line in lines[:separator_idx]:
        before, after = map(int, line.split('|'))
        rules.append((before, after))
    
    # Parse updates
    updates = []
    for line in lines[separator_idx + 1:]:
        pages = list(map(int, line.split(',')))
        updates.append(pages)
    
    return rules, updates

def is_valid_order(pages: List[int], rules: List[Tuple[int, int]]) -> bool:
    """
    Check if a sequence of pages follows all applicable ordering rules.
    
    Args:
        pages (List[int]): List of page numbers in the sequence
        rules (List[Tuple[int, int]]): List of ordering rules
    
    Returns:
        bool: True if the sequence follows all applicable rules
    """
    # Create a set of pages in this update for quick lookup
    page_set = set(pages)
    
    # Create a dictionary to store each page's position
    positions = {page: idx for idx, page in enumerate(pages)}
    
    # Check each rule
    for before, after in rules:
        # Skip rules that don't apply to this update
        if before not in page_set or after not in page_set:
            continue
            
        # If the rule applies, check if the pages are in correct order
        if positions[before] >= positions[after]:
            return False
    
    return True

def get_middle_page(pages: List[int]) -> int:
    """
    Get the middle page number from a sequence.
    
    Args:
        pages (List[int]): List of page numbers
    
    Returns:
        int: The middle page number
    """
    return pages[len(pages) // 2]

def solve_part1(input_data: Tuple[List[Tuple[int, int]], List[List[int]]]) -> int:
    """
    Solve Part 1 of the puzzle.
    
    Args:
        input_data: Tuple containing rules and updates
    
    Returns:
        Sum of middle page numbers from correctly ordered updates
    """
    rules, updates = input_data
    
    # Find valid updates and their middle pages
    middle_sum = 0
    for update in updates:
        if is_valid_order(update, rules):
            middle_sum += get_middle_page(update)
    
    return middle_sum

def build_graph(pages: List[int], rules: List[Tuple[int, int]]) -> Tuple[Dict[int, Set[int]], Dict[int, int]]:
    """
    Build a directed graph and count incoming edges for the given pages and rules.
    
    Args:
        pages (List[int]): List of pages to include in the graph
        rules (List[Tuple[int, int]]): List of ordering rules
    
    Returns:
        Tuple containing:
        - Dictionary mapping each page to its neighbors
        - Dictionary mapping each page to its incoming edge count
    """
    # Create adjacency list representation
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    page_set = set(pages)
    
    # Initialize in_degree for all pages
    for page in pages:
        in_degree[page] = 0
    
    # Build graph using only rules that apply to the given pages
    for before, after in rules:
        if before in page_set and after in page_set:
            graph[before].add(after)
            in_degree[after] += 1
    
    return graph, in_degree

def topological_sort(pages: List[int], rules: List[Tuple[int, int]]) -> List[int]:
    """
    Perform topological sort on the pages using Kahn's algorithm.
    
    Args:
        pages (List[int]): List of pages to sort
        rules (List[Tuple[int, int]]): List of ordering rules
    
    Returns:
        List[int]: Pages in topologically sorted order
    """
    # Build the graph
    graph, in_degree = build_graph(pages, rules)
    
    # Initialize queue with nodes that have no incoming edges
    queue = deque([page for page in pages if in_degree[page] == 0])
    result = []
    
    # Process queue
    while queue:
        # Get node with no incoming edges
        current = queue.popleft()
        result.append(current)
        
        # Remove edges from current node
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

def solve_part2(input_data: Tuple[List[Tuple[int, int]], List[List[int]]]) -> int:
    """
    Solve Part 2 of the puzzle.
    
    Args:
        input_data: Tuple containing rules and updates
    
    Returns:
        Sum of middle page numbers from corrected invalid updates
    """
    rules, updates = input_data
    middle_sum = 0
    
    for update in updates:
        # Only process invalid updates
        if not is_valid_order(update, rules):
            # Sort the pages according to rules
            sorted_pages = topological_sort(update, rules)
            # Add the middle page to the sum
            middle_sum += get_middle_page(sorted_pages)
    
    return middle_sum

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