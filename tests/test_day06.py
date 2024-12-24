### AI Generated Content ###

import pytest
from src.day06 import solve_part1, solve_part2, Lab, Direction, Guard

@pytest.fixture
def example_input():
    return [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#..."
    ]

def test_guard_initial_position(example_input):
    lab = Lab(example_input)
    assert lab.guard.x == 5
    assert lab.guard.y == 6
    assert lab.guard.facing == Direction.UP

def test_guard_movement():
    # Test single guard movement
    guard = Guard(5, 6, Direction.UP)
    guard.move()
    assert guard.get_position() == (5, 5)
    
    # Test turning right
    guard.facing = guard.facing.turn_right()
    assert guard.facing == Direction.RIGHT
    guard.move()
    assert guard.get_position() == (6, 5)

def test_obstacle_detection(example_input):
    lab = Lab(example_input)
    # Test obstacle detection for a known obstacle
    assert lab.is_obstacle(4, 0) == True  # '#' at position (4,0)
    # Test empty space
    assert lab.is_obstacle(0, 0) == False  # '.' at position (0,0)
    # Test out of bounds
    assert lab.is_obstacle(-1, 0) == True
    assert lab.is_obstacle(0, -1) == True
    assert lab.is_obstacle(10, 0) == True
    assert lab.is_obstacle(0, 10) == True

def test_patrol_example(example_input):
    """Test the full patrol simulation with the example input"""
    assert solve_part1(example_input) == 41

def test_patrol_visited_positions(example_input):
    lab = Lab(example_input)
    visited = lab.simulate_patrol()
    # Test a few key positions we know should be visited based on the example output
    assert (5, 6) in visited  # Starting position
    assert (5, 1) in visited  # Top of first vertical movement
    assert (9, 1) in visited  # Right side after first turn
    assert (7, 9) not in visited  # Position we know shouldn't be visited

def test_bounds_checking(example_input):
    lab = Lab(example_input)
    assert lab.is_out_of_bounds(-1, 0) == True
    assert lab.is_out_of_bounds(0, -1) == True
    assert lab.is_out_of_bounds(10, 0) == True
    assert lab.is_out_of_bounds(0, 10) == True
    assert lab.is_out_of_bounds(5, 5) == False

# Placeholder for Part 2 tests
@pytest.mark.skip(reason="Part 2 not implemented yet")
def test_part2_example(example_input):
    assert solve_part2(example_input) == None  # Replace None with expected value when Part 2 is revealed