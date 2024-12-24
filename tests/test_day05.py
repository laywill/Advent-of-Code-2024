### AI Generated Content ###

import pytest
from src.day05 import (
    read_input,
    solve_part1,
    solve_part2,
    is_valid_order,
    topological_sort
)

@pytest.fixture
def example_input():
    """
    Fixture providing the example input from the puzzle description.
    """
    rules = [
        (47, 53),
        (97, 13),
        (97, 61),
        (97, 47),
        (75, 29),
        (61, 13),
        (75, 53),
        (29, 13),
        (97, 29),
        (53, 29),
        (61, 53),
        (97, 53),
        (61, 29),
        (47, 13),
        (75, 47),
        (97, 75),
        (47, 61),
        (75, 61),
        (47, 29),
        (75, 13),
        (53, 13),
    ]
    
    updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    
    return rules, updates

def test_is_valid_order(example_input):
    """
    Test the is_valid_order function with known valid and invalid sequences.
    """
    rules, updates = example_input
    
    # Test known valid sequences
    assert is_valid_order(updates[0], rules) == True  # 75,47,61,53,29
    assert is_valid_order(updates[1], rules) == True  # 97,61,53,29,13
    assert is_valid_order(updates[2], rules) == True  # 75,29,13
    
    # Test known invalid sequences
    assert is_valid_order(updates[3], rules) == False  # 75,97,47,61,53
    assert is_valid_order(updates[4], rules) == False  # 61,13,29
    assert is_valid_order(updates[5], rules) == False  # 97,13,75,29,47

def test_topological_sort(example_input):
    """
    Test the topological_sort function with known invalid sequences.
    """
    rules, updates = example_input
    
    # Test known invalid sequences and their correct orderings
    assert topological_sort([75, 97, 47, 61, 53], rules) == [97, 75, 47, 61, 53]
    assert topological_sort([61, 13, 29], rules) == [61, 29, 13]
    assert topological_sort([97, 13, 75, 29, 47], rules) == [97, 75, 47, 29, 13]

def test_solve_part1(example_input):
    """
    Test part 1 solution with example input.
    """
    assert solve_part1(example_input) == 143

def test_solve_part2(example_input):
    """
    Test part 2 solution with example input.
    """
    assert solve_part2(example_input) == 123