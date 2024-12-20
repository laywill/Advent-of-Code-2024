### AI Generated Content ###

from src.day03 import solve_part1, solve_part2

def test_part1_example():
    """
    Test Part 1 with the example from the problem description:
    'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    Should find: mul(2,4), mul(5,5), mul(11,8), mul(8,5)
    Total should be: 2*4 + 5*5 + 11*8 + 8*5 = 161
    """
    test_input = [
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ]
    
    result = solve_part1(test_input)
    assert result == 161, f"Expected 161, but got {result}"

def test_part2_example():
    """
    Test Part 2 with the example from the problem description:
    'xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))'
    Should only count: mul(2,4) and mul(8,5) due to don't() and do() instructions
    Total should be: 2*4 + 8*5 = 48
    """
    test_input = [
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
    ]
    
    result = solve_part2(test_input)
    assert result == 48, f"Expected 48, but got {result}"

def test_multiple_lines():
    """
    Test both parts with multiple lines of input to ensure proper line handling
    """
    test_input = [
        "xmul(2,4)mul(3,3)",
        "mul(5,5)mul(2,2)"
    ]
    
    # Part 1: All valid multiplications should be counted
    part1_result = solve_part1(test_input)
    assert part1_result == 47, f"Part 1: Expected 47, but got {part1_result}"  # (2*4 + 3*3 + 5*5 + 2*2)
    
    # Part 2: All multiplications should be counted (no do/don't instructions)
    part2_result = solve_part2(test_input)
    assert part2_result == 47, f"Part 2: Expected 47, but got {part2_result}"

def test_empty_input():
    """
    Test both parts with empty input to ensure proper handling
    """
    test_input = []
    
    part1_result = solve_part1(test_input)
    assert part1_result == 0, f"Part 1: Expected 0 for empty input, but got {part1_result}"
    
    part2_result = solve_part2(test_input)
    assert part2_result == 0, f"Part 2: Expected 0 for empty input, but got {part2_result}"