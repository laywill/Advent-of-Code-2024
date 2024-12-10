# Day03 Write-Up 

## Developing on Android

Nothing major to report.

Still kind of slow and annoying. Still wouldn't write bulk code this way.

## LLM Choice

Claude Haiku, worked yesterday, so I probably won't change until it fails to generate a valid solution. 

## Problem

Another trivial problem at first glance needing sone Regex to find valid strings

My immediate gut feel was:
- parse
- Use [regex101.com](https://regex1co.com) to figure out the right RegEx to ignore / include characters
- Write a function to apply tthe regex

I expect part2 will be a change to what is a valid function.

## Prompt and Answers

I'm now convinced that for these easy problems there isnt much prompt engineering required.

Claude however had reached the token limit so I had to start a new chat. I decided to write a generic primer Prompt that will allow me to use a new chat with any LLM:

```
You are an expert Python 3 programmer who will code solutions to the Advent of Code. Each puzzle has two parts: part 1 must be solved to unlock part 2. Part 1 and part 2 use the same input data. I will supply an input to each file in a text file. The solution will need to read in this text file.

You will write Python code, reading input from a file, following this template:


````
```
import pathlib

def read_input(day_number):
    """
    Read input from a text file.
    
    Args:
        day_number (int): Day number of the puzzle
    
    Returns:
        list: Lines from the input file, or processed input as needed
    """
    # Construct the path to the input file
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'

    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def solve_part1(input_data):
    """
    Solve Part 1 of the puzzle.
    
    Args:
        input_data (list): Processed input data
    
    Returns:
        Result of Part 1 solution
    """
    # Implement Part 1 solution here
    pass

def solve_part2(input_data):
    """
    Solve Part 2 of the puzzle.
    
    Args:
        input_data (list): Processed input data
    
    Returns:
        Result of Part 2 solution
    """
    # Implement Part 2 solution here
    pass

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
```
````

Confirm you are ready to solve a puzzle.

```

Claude Haiku accepted this and confirmed it was ready to code.

Response:

```
 I am ready to solve an Advent of Code puzzle! The template you've provided is an excellent approach for solving the challenges. It includes:

- A flexible input reading function that can read from a file in an 'inputs' directory
- Separate functions for solving Part 1 and Part 2
- A main function that automatically detects the day number and runs both parts
- Proper use of Python's `pathlib` for cross-platform file path handling

I'll wait for you to provide the specific puzzle details and input file for the day's challenge. When you do, I'll:
1. Carefully read the puzzle description
2. Analyze the input data
3. Develop a solution for Part 1
4. Solve Part 2, which often requires an extension or modification of the Part 1 approach

Please go ahead and share the puzzle details and input file contents, and I'll get started on creating the solution!
```

### Part 1

I thought it would be interesting to test my primer prompt by just shoving the whole problem in and asking it for a solution.

The Prompt:

```plaintext
Here is the Day 3 Puzzle:

````
```
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
```
````

```

The response:

```
  I'll solve this puzzle step by step. The key challenges here are:
1. Parse through a string of corrupted memory
2. Extract only valid `mul(X,Y)` instructions
3. Multiply the numbers in each valid instruction
4. Sum up all the multiplication results

Here's a solution that handles the specific parsing requirements:


<antArtifact identifier="day03-solution" type="application/vnd.ant.code" language="python" title="Day 3: Corrupted Memory Multiplication">
</antArtifact>

Key aspects of the solution:

1. The `solve_part1` function uses a regular expression to find valid `mul(X,Y)` instructions:
   - `mul\s*\(` matches `mul(` with optional whitespace
   - `(\d{1,3})` captures 1-3 digit numbers for X and Y
   - `\s*,\s*` allows for whitespace around the comma
   - The regex is flexible enough to ignore invalid characters and malformed instructions

2. It extracts the numbers, converts them to integers, multiplies them
3. Collects the results in a list and returns their sum

The solution handles various edge cases like:
- Whitespace before/after parentheses
- Whitespace between numbers and comma
- Ignoring invalid characters
- Finding multiple `mul` instructions in the same string

I'm ready for you to provide the input file so I can run the solution and verify the result!
```

Claude has been potentially too good. I think, based on the puzzle we need to be exact and unforgiving, rejecting whitespace as invalid.

However, we got the right answer first time. So my reading of the puzzle was less correct than the LLM.

### Part 2

Similar to what I expected. Same RegEx, two new ones, and having whether results can be valid or not.
Technically trivial, but needs a bit of thinking about to not get lost with the do / don't functions. 
I would capture everything then process a list of valid instructions seperately.

The Prompt:

```plaintext
I have run this locally. Your solution worked first time. Now update the solution to solve Part 2:

--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.
There are two new instructions you'll need to handle:
The `do()` instruction enables future mul instructions.
The `don't()` instruction disables future mul instructions.
Only the most recent `do()` or `don't()` instruction applies. At the beginning of the program, `mul` instructions are enabled.

For example:
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications? 
```

The Response:

```plaintext
  I'll update the solution to handle the new `do()` and `don't()` instructions for Part 2:


<antArtifact identifier="day03-solution" type="application/vnd.ant.code" language="python" title="Day 3: Corrupted Memory Multiplication with Conditional Instructions">
</antArtifact>

Key changes for Part 2:

1. Added new regex patterns for `do()` and `don't()` instructions
   - Handles variations like `do()`, `don't()`, and `dont()`
   - Allows for optional whitespace

2. Implemented a state tracking mechanism:
   - `mul_enabled` starts as `True`
   - `do()` instruction sets `mul_enabled` to `True`
   - `don't()` instruction sets `mul_enabled` to `False`

3. Modified the scanning approach:
   - Iterates through the input string
   - Checks for `do()`, `don't()`, and `mul()` instructions in order
   - Only adds multiplication results when `mul_enabled` is `True`
   - Moves position forward after each match

The solution handles the example cases:
- Disabling `mul` instructions with `don't()`
- Re-enabling `mul` instructions with `do()`
- Tracking the most recent enable/disable instruction

I recommend running this solution with the provided input file to verify the Part 2 result. The approach is flexible and should handle various edge cases in the corrupted memory string.
```

Comment on LLM output

Comment on whether it worked

## Solution

Overall comment