### AI Generated Content ###

import pytest
from src.day03 import solve_part1, solve_part2

def test_part1_example():
    """Test Part 1 with the example from the problem description"""
    example_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert solve_part1(example_input) == 161

def test_part2_example():
    """Test Part 2 with the example from the problem description"""
    example_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert solve_part2(example_input) == 48

def test_part2_multiple_instructions():
    """Test Part 2 with multiple do() and don't() instructions"""
    example_input = "do()mul(1,2)don't()mul(3,4)do()mul(5,6)"
    assert solve_part2(example_input) == 35  # 1*2 + 5*6

def test_part2_initial_state():
    """Verify that mul instructions start enabled"""
    example_input = "mul(7,8)don't()mul(9,10)"
    assert solve_part2(example_input) == 56  # Only 7*8 should be calculated