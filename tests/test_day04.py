### AI Generated Content ###

import pytest
from src.day04 import solve_part1, solve_part2

def test_part1_example():
    """Test Part 1 with the example from the puzzle description"""
    example_input = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    assert solve_part1(example_input) == 18

def test_part2_example():
    """Test Part 2 with the example from the puzzle description"""
    example_input = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    assert solve_part2(example_input) == 9

def test_part2_simple_example():
    """Test Part 2 with the simple X-MAS example from the puzzle description"""
    example_input = [
        "M.S",
        ".A.",
        "M.S"
    ]
    # The puzzle mentions this pattern has 6 valid permutations
    assert solve_part2(example_input) == 6