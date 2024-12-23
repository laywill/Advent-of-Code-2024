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

def test_part1_dotted_example():
    """Test Part 1 with the example where non-XMAS letters are replaced with dots"""
    example_input = [
        "....XXMAS.",
        ".SAMXMS...",
        "...S..A...",
        "..A.A.MS.X",
        "XMASAMX.MM",
        "X.....XA.A",
        "S.S.S.S.SS",
        ".A.A.A.A.A",
        "..M.M.M.MM",
        ".X.X.XMASX"
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

def test_part2_dotted_example():
    """Test Part 2 with the example where non-X-MAS letters are replaced with dots"""
    example_input = [
        ".M.S......",
        "..A..MSMS.",
        ".M.S.MAA..",
        "..A.ASMSM.",
        ".M.S.M....",
        "..........",
        "S.S.S.S.S.",
        ".A.A.A.A..",
        "M.M.M.M.M.",
        ".........."
    ]
    assert solve_part2(example_input) == 9

def test_part2_simple_ms_on_left():
    """Test Part 2 with simple X-MAS pattern - Ms on left"""
    example_input = [
        "M.S",
        ".A.",
        "M.S"
    ]
    assert solve_part2(example_input) == 1

def test_part2_simple_ms_on_top():
    """Test Part 2 with simple X-MAS pattern - Ms on top"""
    example_input = [
        "M.M",
        ".A.",
        "S.S"
    ]
    assert solve_part2(example_input) == 1

def test_part2_simple_ms_on_bottom():
    """Test Part 2 with simple X-MAS pattern - Ms on bottom"""
    example_input = [
        "S.S",
        ".A.",
        "M.M"
    ]
    assert solve_part2(example_input) == 1

def test_part2_simple_ms_on_right():
    """Test Part 2 with simple X-MAS pattern - Ms on right"""
    example_input = [
        "S.M",
        ".A.",
        "S.M"
    ]
    assert solve_part2(example_input) == 1

def test_part2_all_patterns_should_total_four():
    """Test that running part2 on all valid patterns gives us 4 total"""
    # Create all four test patterns
    patterns = [
        ["M.S", ".A.", "M.S"],  # Ms on left
        ["M.M", ".A.", "S.S"],  # Ms on top
        ["S.S", ".A.", "M.M"],  # Ms on bottom
        ["S.M", ".A.", "S.M"],  # Ms on right
    ]
    
    # Each pattern should find exactly one X-MAS
    total = sum(solve_part2(pattern) for pattern in patterns)
    assert total == 4