# Day04 Write-Up 

## Developing on Android

Nothing major to report.

Still kind of slow and annoying. Still wouldn't write bulk code this way.

## LLM Choice

Claude 3.5 Sonnet. I was offered it yesterday and liked it.

I kept running out of messages, hitting my daily limit etc and was getting annoyed having to start new chats etc, so I took the plunge and bought a month's subscription to Claude Pro.
I didn't use the projects feature - just continued to use my "one chat per day" approach.

## Problem

A classic advent of code sub-strings in strings finding, with an amusing twist of forwards, backwards, horizontal, vertical and diagonal.

My immediate gut feel was to brute force this - iterate through starting locations, use that to search all 4 directions.
Either do boundary checking, or pad the boundary with invalid characters so that it will fail.

Part 2 was unsurprising - reuse the diagonal bit of the search function, but then double validate, and with some additional spiciness.

## Prompt and Answers

Standard setup prompt:

> You are an expert Python 3 programmer who will code solutions to the Advent of Code. Each puzzle has two parts: part 1 must be solved to unlock part 2. Part 1 and part 2 use the same input data. I will supply an input to each file in a text file. The solution will need to read in this text file.
> 
> You will write Python code, reading input from a file, following this template:
> 
> ```
> import pathlib
> 
> def read_input(day_number):
>     """
>     Read input from a text file.
>     
>     Args:
>         day_number (int): Day number of the puzzle
>     
>     Returns:
>         list: Lines from the input file, or processed input as needed
>     """
>     # Construct the path to the input file
>     current_dir = pathlib.Path(__file__).parent.parent
>     input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'
> 
>     with open(input_path, 'r') as f:
>         return [line.strip() for line in f.readlines()]
> 
> def solve_part1(input_data):
>     """
>     Solve Part 1 of the puzzle.
>     
>     Args:
>         input_data (list): Processed input data
>     
>     Returns:
>         Result of Part 1 solution
>     """
>     # Implement Part 1 solution here
>     pass
> 
> def solve_part2(input_data):
>     """
>     Solve Part 2 of the puzzle.
>     
>     Args:
>         input_data (list): Processed input data
>     
>     Returns:
>         Result of Part 2 solution
>     """
>     # Implement Part 2 solution here
>     pass
> 
> def main():
>     # Automatically extract day number from filename
>     day_number = int(pathlib.Path(__file__).stem[3:])
> 
>     # Read input
>     input_data = read_input(day_number)
> 
>     # Solve Part 1
>     part1_solution = solve_part1(input_data)
>     print(f"Day {day_number} - Part 1 Solution: {part1_solution}")
> 
>     # Solve Part 2
>     part2_solution = solve_part2(input_data)
>     print(f"Day {day_number} - Part 2 Solution: {part2_solution}")
> 
> if __name__ == '__main__':
>     main()
> ```
> 
> Confirm you are ready to solve a puzzle.

Response:

> I'm ready to help solve Advent of Code puzzles! I'll use the template you provided and write clean, efficient Python 3 solutions. The template includes a proper file reading structure and separate functions for each part of the puzzle.
> 
> For each puzzle you present, I will:
> 1. Implement the solution following the given template
> 2. Write clear, well-documented code
> 3. Handle both Part 1 and Part 2
> 4. Include any necessary helper functions or data structures
> 5. Use appropriate Python features and best practices
> 
> Please provide the puzzle description and I'll help you solve it.

### Part 1

Part 1 was relatively simple, well defined, and needed only a trivial amount of re-factoring to make it explicit for the LLM before I fed it in.

The Prompt:

> Ok, here we go with Day 4 Part 1:
> 
> --- Day 4: Ceres Search ---
> "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!
> 
> As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: `XMAS`.
> 
> This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of `XMAS` - you need to find all of them. Here are a few ways `XMAS` might appear, where irrelevant characters have been replaced with .:
> 
> ```
> ..X...
> .SAMX.
> .A..A.
> XMAS.S
> .X....
> ```
> 
> Note that this demonstrates all four valid appearances of `XMAS`: left-to-right, right-to-left, top-to-bottom and bittom-to-top.
> 
> The actual word search will be full of letters instead. For example:
> 
> ```
> MMMSXXMASM
> MSAMXMSMSA
> AMXSXMAAMM
> MSAMASMSMX
> XMASAMXAMM
> XXAMMXXAMA
> SMSMSASXSS
> SAXAMASAAA
> MAMMMXMMMM
> MXMXAXMASX
> ```
> 
> In this word search, `XMAS` occurs a total of 18 times; here's the same word search again, but where letters not involved in any `XMAS` have been replaced with `.`:
> 
> ```
> ....XXMAS.
> .SAMXMS...
> ...S..A...
> ..A.A.MS.X
> XMASAMX.MM
> X.....XA.A
> S.S.S.S.SS
> .A.A.A.A.A
> ..M.M.M.MM
> .X.X.XMASX
> ```
> 
> Take a look at the little Elf's word search. How many times does `XMAS` appear?

The response:

> I'll help you solve this word search puzzle to find all instances of "XMAS" in any direction. Let's write a solution that checks all possible directions: horizontal (left-to-right and right-to-left), vertical (top-to-bottom and bottom-to-top), and diagonal (all four diagonal directions).
> 
> <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution">
> ...
> </antArtifact>
> 
> This solution includes:
> 
> 1. The required file reading functionality as per the template
> 2. A helper function `check_direction()` that checks if "XMAS" exists starting from a given position in a specific direction
> 3. A main solving function that:
>    - Iterates through every position in the grid
>    - Checks all eight possible directions from each position
>    - Counts the total number of "XMAS" occurrences
> 
> The solution will find all instances of "XMAS" in:
> - Horizontal (left-to-right and right-to-left)
> - Vertical (top-to-bottom and bottom-to-top)
> - All four diagonal directions
> 
> The `solve_part2()` function is currently a placeholder since Part 2 hasn't been revealed yet.
> 
> You can run this code with your input file and it will output the total number of times "XMAS" appears in the word search. Would you like me to explain any part of the solution in more detail?

Clean tidy solution that worked straight away.
Exactly what I am coming to expect from Claude and these LLM solutions.

### Part 2

#### Setup for Failure

Lots of potential for reuse and refactoring today, which was interesting to try with the LLM.

Now... my first big mistake:
In previous days, part 2 has started to need a bit more guiding.
I tried to pre-empt this by editing the prompt to try and be helpful.

However, I was rushing to try and get this done on my lunch break and misread the problem so thought that as well as the 4 obvious rotations of the provided example X-MAS, there were two other potentials:


```
# M top left and bottom right:
M.S
.A.
S.M
```

```
# M top right and bottom left:
S.M
.A.
M.S
```

Clearly these diagonals do not read `MAS` or `SAM`. So, I feel I made a rod for my own back here as this led the LLM down the path of thinking the cardinal directions still needed considering as well as the diagonals.

This all ended up taking a while to realise, and unpick.

I also ended up then missing that it had got other trivial errors, so all in all - my bad!

#### The tale plays out

The Prompt:

> Fantastic work - your solution worked first time and got the right answer! Now for Part 2:
> 
> --- Part Two ---
> The Elf looks quizzically at you. Did you misunderstand the assignment?
> Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an `X-MAS` puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
> 
> ```
> M.S
> .A.
> M.S
> ```
> 
> Note, that as before that the `X-MAS` example pattern has 6 valid search permutations. Let me know if you need me to provide these explicitly.
> 
> Irrelevant characters have again been replaced with `.` in the above diagram. Within the `X`, each `MAS` can be written forwards or backwards.
> Here's the same example from before, but this time all of the `X-MAS`es have been kept instead:
> 
> ```
> .M.S......
> ..A..MSMS.
> .M.S.MAA..
> ..A.ASMSM.
> .M.S.M....
> ..........
> S.S.S.S.S.
> .A.A.A.A..
> M.M.M.M.M.
> ..........
> ```
> 
> In this example, an `X-MAS` appears 9 times.
> Flip the word search from the instructions back over to the word search side and try again. How many times does an `X-MAS` appear?

The Response:

> Ah, interesting twist! Now we need to find "X" patterns where each arm contains "MAS" (forwards or backwards). Let me modify the solution to handle this new pattern.
> 
> ```python
> import pathlib
> 
> def read_input(day_number):
>     """
>     Read input from a text file.
>     
>     Args:
>         day_number (int): Day number of the puzzle
>     
>     Returns:
>         list: Lines from the input file as a list of strings
>     """
>     current_dir = pathlib.Path(__file__).parent.parent
>     input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'
> 
>     with open(input_path, 'r') as f:
>         return [line.strip() for line in f.readlines()]
> 
> def check_direction(grid, row, col, dr, dc, target="XMAS"):
>     """
>     Check if the target word exists starting from a position in a given direction.
>     
>     Args:
>         grid (list): The word search grid
>         row (int): Starting row
>         col (int): Starting column
>         dr (int): Row direction (-1, 0, or 1)
>         dc (int): Column direction (-1, 0, or 1)
>         target (str): The word to find (default: "XMAS")
>     
>     Returns:
>         bool: True if the word is found in this direction, False otherwise
>     """
>     if (
>         row + dr * (len(target) - 1) < 0 
>         or row + dr * (len(target) - 1) >= len(grid)
>         or col + dc * (len(target) - 1) < 0 
>         or col + dc * (len(target) - 1) >= len(grid[0])
>     ):
>         return False
>     
>     for i in range(len(target)):
>         if grid[row + dr * i][col + dc * i] != target[i]:
>             return False
>     return True
> 
> def check_mas_direction(grid, row, col, dr, dc):
>     """
>     Check if "MAS" exists starting from a position in a given direction.
>     Also checks for "SAM" in the same direction.
>     
>     Args:
>         grid (list): The word search grid
>         row (int): Starting row
>         col (int): Starting column
>         dr (int): Row direction (-1, 0, or 1)
>         dc (int): Column direction (-1, 0, or 1)
>     
>     Returns:
>         bool: True if either "MAS" or "SAM" is found in this direction
>     """
>     return check_direction(grid, row, col, dr, dc, "MAS") or check_direction(grid, row, col, dr, dc, "SAM")
> 
> def check_x_mas(grid, center_row, center_col):
>     """
>     Check if there's a valid X-MAS pattern centered at the given position.
>     An X-MAS pattern consists of two "MAS" strings (or "SAM") forming an X.
>     
>     Args:
>         grid (list): The word search grid
>         center_row (int): Row of the center of the X
>         center_col (int): Column of the center of the X
>     
>     Returns:
>         bool: True if a valid X-MAS pattern is found
>     """
>     # Check all four possible combinations of diagonal MAS patterns
>     diagonal_pairs = [
>         # Upper-left to lower-right AND upper-right to lower-left
>         [(-1, -1, 1, 1), (-1, 1, 1, -1)],
>         # Lower-right to upper-left AND lower-left to upper-right
>         [(1, 1, -1, -1), (1, -1, -1, 1)]
>     ]
>     
>     for dr1, dc1, dr2, dc2 in diagonal_pairs:
>         # Check if we can find MAS (or SAM) in both diagonals
>         if check_mas_direction(grid, center_row, center_col, dr1, dc1) and \
>            check_mas_direction(grid, center_row, center_col, dr2, dc2):
>             return True
>             
>     return False
> 
> def solve_part1(input_data):
>     """
>     Solve Part 1 of the puzzle.
>     
>     Args:
>         input_data (list): List of strings representing the word search grid
>     
>     Returns:
>         int: Total number of times XMAS appears in the grid
>     """
>     grid = input_data
>     height = len(grid)
>     width = len(grid[0])
>     count = 0
>     
>     # Define all eight directions
>     directions = [
>         (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
>         (0, -1),           (0, 1),    # Left, Right
>         (1, -1),  (1, 0),  (1, 1)     # Down-left, Down, Down-right
>     ]
>     
>     # Check every starting position
>     for row in range(height):
>         for col in range(width):
>             # Check all eight directions from this position
>             for dr, dc in directions:
>                 if check_direction(grid, row, col, dr, dc):
>                     count += 1
>     
>     return count
> 
> def solve_part2(input_data):
>     """
>     Solve Part 2 of the puzzle.
>     
>     Args:
>         input_data (list): List of strings representing the word search grid
>     
>     Returns:
>         int: Total number of X-MAS patterns found
>     """
>     grid = input_data
>     height = len(grid)
>     width = len(grid[0])
>     count = 0
>     
>     # Check every possible center position for an X pattern
>     # We need at least 2 spaces in each direction for a complete X-MAS
>     for row in range(1, height - 1):
>         for col in range(1, width - 1):
>             if check_x_mas(grid, row, col):
>                 count += 1
>     
>     return count
> 
> def main():
>     # Automatically extract day number from filename
>     day_number = int(pathlib.Path(__file__).stem[3:])
> 
>     # Read input
>     input_data = read_input(day_number)
> 
>     # Solve Part 1
>     part1_solution = solve_part1(input_data)
>     print(f"Day {day_number} - Part 1 Solution: {part1_solution}")
> 
>     # Solve Part 2
>     part2_solution = solve_part2(input_data)
>     print(f"Day {day_number} - Part 2 Solution: {part2_solution}")
> 
> if __name__ == '__main__':
>     main()
> 
> ```
> 
> For Part 2, I've made the following changes:
> 
> 1. Added a new helper function `check_mas_direction()` that checks for both "MAS" and "SAM" in a given direction
> 2. Added a new function `check_x_mas()` that checks for valid X-MAS patterns by:
>    - Looking for two diagonal "MAS" or "SAM" strings that form an X
>    - Checking all possible combinations of forwards and backwards "MAS"
> 3. Modified `solve_part2()` to:
>    - Iterate through all possible center positions in the grid
>    - Count the total number of valid X-MAS patterns
> 
> The solution accounts for:
> - Both arms of the X must contain "MAS" (or "SAM")
> - Each "MAS" can be written forwards or backwards
> - The pattern must form an X shape
> 
> You can run this with your input and it will count all valid X-MAS patterns in the grid. Would you like me to explain any part of the solution in more detail?

You can see the LLM had the decency to ignore my complete nonsense about there being 6 possible matches, and instead came up with a lovely elegant solution.
It didn't work though.

Bluntly telling it such was surprisingly effective at getting it to run:

Prompt:

> I like your approach, but we can an error when trying to run it. Please fix the error:
> 
> ```
> === Running day04 ===
> Traceback (most recent call last):
>   File "/home/runner/work/Advent-of-Code-2024/Advent-of-Code-2024/src/day04.py", line 167, in <module>
> Day 4 - Part 1 Solution: 2462
>     main()
>   File "/home/runner/work/Advent-of-Code-2024/Advent-of-Code-2024/src/day04.py", line 163, in main
>     part2_solution = solve_part2(input_data)
>                      ^^^^^^^^^^^^^^^^^^^^^^^
>   File "/home/runner/work/Advent-of-Code-2024/Advent-of-Code-2024/src/day04.py", line 146, in solve_part2
>     if check_x_mas(grid, row, col):
>        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
>   File "/home/runner/work/Advent-of-Code-2024/Advent-of-Code-2024/src/day04.py", line 87, in check_x_mas
>     for dr1, dc1, dr2, dc2 in diagonal_pairs:
>         ^^^^^^^^^^^^^^^^^^
> ValueError: not enough values to unpack (expected 4, got 2)
> ```

The response:

> Ah, I see the error. The diagonal_pairs list structure is incorrect. Let me fix the format of the diagonal pairs.
> 
> <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> ...
> </antArtifact>
> 
> The key fix was in the `diagonal_pairs` structure inside `check_x_mas()`. I've changed it to properly pair the diagonal directions:
> - Each pair now consists of two tuples, where each tuple contains the direction for one arm of the X
> - The format is now `((-1, -1), (1, 1))` and `((-1, 1), (1, -1))` representing the two possible X orientations
> - This allows proper unpacking in the loop with `for (dr1, dc1), (dr2, dc2) in diagonal_pairs`
> 
> The solution should now run without errors. Would you like me to explain any other part of the solution?

And run it did, but generating the wrong answer.

#### Adding Tests

Having done this for Day 03 I had a prepared prompt that handled creating a PyTest for this and using only the provided example input.

I had to prompt it to add the dotted examples in addition to the non-dotted examples.

This wasn't particularly exciting, and Claude handled it easily.

Here I led it astray by trying to add test cases that included the two clearly incorrect ones:

> `test_part2_simple_example()` is failing, so we need to fix the `part2()` and / or `check_x_mas()` functions.
> 
> The current test uses this input (we'll refer to this as "Ms on left"):
> 
> ```
> M.S
> .A.
> M.S
> ```
> 
> The other 5 valid inputs are:
> 
> "Ms on top": 
> 
> ```
> M.M
> .A.
> S.S
> ```
> 
> "Ms on bottom":
> 
> ```
> S.S
> .A.
> M.M
> ```
> 
> "Ms on right"
> 
> ```
> S.M
> .A.
> S.M
> ```
> 
> "Ms top left and bottom right":
> 
> ```
> M.S
> .A.
> S.M
> ```
> 
> "Ms top right and bottom left":
> 
> ```
> S.M
> .A.
> M.S
> ```
> 
> Update the tests to add these additional sinple test cases for part2.

The Response:

> I'll extend the test cases to include all six valid X-MAS patterns explicitly.
> 
> <antArtifact identifier="day04-tests" type="application/vnd.ant.code" language="python" title="Pytest file for Day 4">
> ...
> </antArtifact>
> 
> I've added:
> 1. Individual test cases for each of the six valid X-MAS patterns
> 2. A composite test that verifies that all patterns together sum to 6
> 3. Clear docstrings explaining each pattern variation
> 4. Each individual test asserts that it finds exactly one X-MAS pattern
> 5. Kept the original complex test cases for both full and dotted versions
> 
> Now that we have comprehensive test coverage for all valid patterns, we can use these tests to debug and fix our `check_x_mas()` function. The failures should help us identify which patterns we're missing in our current implementation.
> 
> Would you like me to analyze the test results and suggest fixes for the `check_x_mas()` function?

Rather nice of it to add a test for each of my provided inputs and then another composite test to test all of them together.
It's little things like this that I think the LLM is really good at - it suggests things I otherwise might not have thought were useful.

#### The moment of self sabotage

I realised my mistake:

> I made a mistake! There are only 4 valid solutions for an X-MAS in part 2
> 
> - "Ms on left"
> - "Ms on top"
> - "Ms on bottom"
> - "Ms on right"
> 
> Update the tests to remove the no longer needed test cases for part2.
> Update the part2 solution to pass these tests.

The Response:

> Ah, that makes more sense - we only need to check for the 4 cardinal directions where both MAS strings extend in opposite directions! Let me update both the tests and the solution.
> 
> <antArtifact identifier="day04-tests" type="application/vnd.ant.code" language="python" title="Pytest file for Day 4">
> ...
> </antArtifact>
> 
> <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> ...
> </antArtifact>
> 
> Key changes:
> 
> 1. In the tests:
>    - Removed the diagonal pattern test cases
>    - Updated the total patterns test to check for 4 instead of 6
>    - Kept only the four valid cardinal direction patterns
> 
> 2. In the solution:
>    - Updated `check_x_mas()` to only check cardinal directions (vertical and horizontal)
>    - Simplified the direction_pairs to only contain:
>      - Vertical pair (up/down)
>      - Horizontal pair (left/right)
>    - Each direction pair now represents opposite directions for finding MAS/SAM patterns
> 
> The solution now correctly handles the four valid X-MAS patterns:
> 1. Vertical with Ms on top
> 2. Vertical with Ms on bottom
> 3. Horizontal with Ms on left
> 4. Horizontal with Ms on right
> 
> Each test case verifies one specific pattern, and we ensure that all four patterns are recognized correctly.


I say this is the moment of self-sabotage because the LLM mentions cardinal directions, which should have been the major hint that it had the wrong end of the stick.
So I started down a line of focussing on whether it was detecting `MAS` and `SAM` (correct line of investigation).


#### Unpicking Cardinal Directions

The prompt:

> Thanks for updating, we now have a better understanding of how the code works (or doesn't work as the case may be). All tests for part2 are failing. This means we are doing something consistently wrong affecting all part2 test cases.
> 
> I think we aren't detecting `MAS` and `SAM` strings correctly.
> In `part1()` we could find a single string (`XMAS`) in any cardinal direction, including diagonals.
> 
> The only way to find a `MAS` or `SAM` string in part2 is to find it on a diagonal (reducing the number of possible directions to search). The trick is finding two valid strings on both diagonals with the same centre coordinates. 
> 
> In the `check_x_mas()` function we call `check_mas_direction()`. I'm not convinced these functions are achieving this. If they are, please explain how.

So, Claude did understand this, and was clearly working on it's reversible directions idea to be able to search diagonals.

> Ah, now I understand the misunderstanding! You're absolutely right - I made a crucial error in the logic. In Part 2:
> 
> 1. The "X" shape implies we must search along diagonals only (not cardinal directions like I incorrectly implemented)
> 2. We need to find MAS/SAM on both diagonals that intersect at a center point
> 3. The diagonal directions would be:
>    - Top-left to bottom-right ((-1, -1) to (1, 1))
>    - Top-right to bottom-left ((-1, 1) to (1, -1))
> 
> Let me update the `check_x_mas` function to handle this correctly:
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> Key changes:
> 
> 1. Completely rewrote `check_x_mas()` to:
>    - Only look for patterns along diagonals
>    - Check both diagonals through the center point
>    - Look for both "MAS" and "SAM" along each diagonal
>    - Consider all possible three-letter strings that can be formed along each diagonal
> 
> 2. Added helper functions inside `check_x_mas()`:
>    - `get_diagonal_strings()`: Gets all possible 3-letter strings along one diagonal
>    - `get_other_diagonal_strings()`: Gets all possible 3-letter strings along the other diagonal
> 
> 3. Simplified the string checking by:
>    - Building complete strings and checking if they match "MAS" or "SAM"
>    - Checking both diagonals through each center point
> 
> This should now correctly find patterns where:
> 1. Each pattern requires two diagonal "MAS"/"SAM" strings that intersect
> 2. The strings must form an X shape
> 3. Each string can be either "MAS" or "SAM"
> 
> Let me know if you'd like me to explain any part of the solution in more detail!

This was a horrible solution (that still didn't work) with the first time I had seen Claude produce a lot of duplicate code.

Refactoring was surprisingly easy though! Prompt:

> Even our simple part2 tests are failing, so we have still missed something.
> 
> Additionally the `get_diagonal_strings()` and get other `diagonal_strings()`  functions seem identical other than where you set `dr` and `dc`. Can this also be refactored to be clearer?

The response was good and did include a refactor:

> You're right on both counts. Let me simplify the diagonal string collection into a single function and also review how we're finding the X patterns.
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> Key changes:
> 1. Combined the duplicate diagonal string functions into a single `get_diagonal_string()` function
> 2. Reorganized the diagonal checking in `check_x_mas()` to more clearly show:
>    - We check both diagonals independently
>    - We collect all possible strings for each diagonal
>    - We look for at least one valid string ("MAS" or "SAM") on each diagonal
> 3. Improved documentation and variable naming for clarity
> 4. Made the diagonal direction pairs more explicit
> 
> Looking at the test failures, I think we still might have an issue with:
> 1. The center point position - we might need to adjust where we start checking from
> 2. The boundaries - we might need to adjust the range we check
> 3. The diagonal string collection - we might need to verify we're getting all valid strings
> 
> Would you like me to run the tests with some debug output to see exactly what strings we're finding (or not finding) in each test case?

#### Closing in on victory

Turns out Claude can't run your code, but it did add the debug statemens:

Prompt:

> Yes please run the tests with debug output.

This for whatever reason yeilded a beautiful result with lovely debug statements, and for some unknown reason a missing function:

Response:

> I'll add debug output to help us understand what's happening with the diagonal string detection.
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> I've added detailed debug output that will show us:
> 1. The input grid state
> 2. Each position being checked
> 3. The diagonal strings being found in each direction
> 4. Boundary check results
> 5. Valid string detection results
> 
> Let's run this with the simplest test case ("Ms on left") first:
> ```python
> example_input = [
>     "M.S",
>     ".A.",
>     "M.S"
> ]
> ```
> 
> This should help us see:
> 1. Where we're looking for strings
> 2. What strings we're actually finding
> 3. Why we might be missing valid patterns
> 4. If our boundary checks are correct
> 
> Would you like me to run the test and share the debug output?

I was starting to get frustrated and blunt. TBH I just wanted this day's problem to be sorted.

The Prompt:

> You got rid of the check_direction function which has broken part 1.
> Put it back in and add debug to it too.

The Response was really good and put it back verbatim 

> Ah yes, sorry about that! Let me restore the check_direction function and add debug output to it as well.
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> Key changes:
> 1. Restored the `check_direction` function
> 2. Added comprehensive debug output to `check_direction` showing:
>    - Starting position and direction
>    - Each character being added to the word
>    - Boundary check results
>    - Final word found and whether it matches
> 3. All functions now show their input grid state
> 4. All functions report their findings clearly
> 
> Let's run this with both the simple test cases like:
> ```python
> # Ms on left
> example_input = [
>     "M.S",
>     ".A.",
>     "M.S"
> ]
> ```
> 
> The debug output should now show us:
> 1. The exact path taken through the grid for both Part 1 and Part 2
> 2. Every string being built and checked
> 3. Any boundary issues
> 4. Why patterns are being matched or not matched
> 
> Would you like me to run the tests with this debug output?


#### Victory

Now with meaningful debug statements I could check the output in CI and it was TOTALLY obvious what was going on.


Frustratingly, Claude actually gave me the clue I needed earlier:

> Looking at the test failures, I think we still might have an issue with:
> 1. The center point position - we might need to adjust where we start checking from
> 2. The boundaries - we might need to adjust the range we check
> 3. The diagonal string collection - we might need to verify we're getting all valid strings

It was iterating through the correct centres but doing absolute nonsense maths to try and get the adjacent diagonal cells.
This shouldn't be totally surprising as it had done maths wrong before when creating tests in day 3's test cases.

The prompt:

> Oh you plonker! In `get_diagonal_string()` you don't do the indexing correctly.
> 
> The if statement should use the absolute magnitude of `dr` and `dc` for boundary checking:
> * `row - abs(dr) <0`
> * `row + abs(dr) > len(grid)`
> * `col - abs(dc) <0`
> * `col + abs(dc) > len(grid[0])`
> 
> I suggest using a similar approach to then build the strings, but without the `abs()` function so that `dr` and `dc` control the direction, e.g:
> 
> ```
> string = (grid[row - dr][col - dc] + 
>             grid[row][col] + 
>             grid[row + dr][col + dc])
> ```
> 
> I think I've got this right. Can you update the solution?

This garnered a weird result - it didn't update the whole solution for the first time, and instead only gave me the updated function.

Reponse:

> Ah yes, that's it! We need to correctly check the boundaries for both directions from the center point, and then collect characters centered on our current position. Let me update the solution.
> 
> ```python
> def get_diagonal_string(grid, row, col, dr, dc):
>     """
>     Get a 3-letter string along a diagonal direction, centered on the given position.
>     
>     Args:
>         grid (list): The word search grid
>         row (int): Center row
>         col (int): Center column
>         dr (int): Row direction (-1 or 1)
>         dc (int): Column direction (-1 or 1)
>     
>     Returns:
>         str: The 3-letter string found along the diagonal, or None if out of bounds
>     """
>     print(f"\nTrying diagonal from ({row},{col}) with direction ({dr},{dc})")
>     
>     # Check if we can get a 3-letter string centered on this position
>     if (row - abs(dr) < 0 or row + abs(dr) >= len(grid) or 
>         col - abs(dc) < 0 or col + abs(dc) >= len(grid[0])):
>         print(f"  Out of bounds! Grid size: {len(grid)}x{len(grid[0])}")
>         print(f"  Would need positions: ({row - abs(dr)},{col - abs(dc)}) to ({row + abs(dr)},{col + abs(dc)})")
>         return None
>     
>     # Build the 3-letter string centered on the current position
>     string = (grid[row - dr][col - dc] + 
>              grid[row][col] + 
>              grid[row + dr][col + dc])
>     print(f"  Found string: {string}")
>     print(f"    from: ({row - dr},{col - dc}) -> ({row},{col}) -> ({row + dr},{col + dc})")
>     return string
> ```
> 
> Key changes:
> 1. Boundary checking now uses `abs(dr)` and `abs(dc)` to ensure we have space in both directions from the center
> 2. String building is now centered on the current position and uses the raw `dr` and `dc` values to control direction
> 3. Added more detailed debug output showing exactly which positions are being checked
> 
> This should now correctly find strings like:
> - From top-left to bottom-right: when checking position (1,1) with dr=1, dc=1, it will look at (0,0), (1,1), (2,2)
> - From bottom-left to top-right: when checking position (1,1) with dr=-1, dc=1, it will look at (2,0), (1,1), (0,2)
> 
> Let me know if you'd like me to run the tests with this update to see if we're now correctly finding the patterns!

I refuse to write a line of code or edit a file manually for this challenge, so here we go again:

Prompt:

> That function looks better, put it into the complete solution

Response:

> I'll update the complete solution with the fixed `get_diagonal_string` function.
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> The key changes were:
> 1. Updated `get_diagonal_string` to properly handle boundaries using `abs()` for checks
> 2. Changed string building to be centered on the current position
> 3. Added more detailed debug output in the diagonal string function
> 
> Now when it checks for a pattern:
> 1. It properly verifies we have space in both directions from the center
> 2. Builds strings centered on the 'A' in the pattern
> 3. Looks in both directions along each diagonal to find the "MAS"/"SAM" strings
> 
> Would you like me to run this with the test cases to see if we're now correctly finding all patterns?

This worked and we got the right answer.

#### Tidying up

Prompt:

> Fantastic, we have solved the problem!
> Now convert all those statements to `logging` statements.
> 
> To speed up running the solution, set the logging level to warnings so that they don't actually get printed to terminal.

Response:

> I'll convert all the print statements to logging statements and set the default level to WARNING.
> 
> > <antArtifact identifier="day04-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 4 Solution Updated">
> > ...
> > </antArtifact>
> 
> Key changes:
> 1. Added proper Python logging configuration at the top of the file
> 2. Set default logging level to WARNING so logs won't appear unless explicitly requested
> 3. Converted all print statements to appropriate logging levels:
>    - DEBUG for detailed tracing information
>    - INFO for general progress information
>    - Only kept print statements for final answers
> 4. Created a module-level logger using `logging.getLogger(__name__)`
> 
> Now you can:
> - Run normally and only see the solutions (logging level WARNING)
> - Enable debug output by changing the level: `logging.basicConfig(level=logging.DEBUG)`
> - Get intermediate information by using INFO level
> - Send logs to a file by adding a file handler to the logging configuration
> 
> Would you like me to show how to enable different logging levels for debugging?

Success - neat tidy output, passing PyTest, and the correct answers.

## Comment on LLM output

It got there. This was by far the biggest slog and beating around the bush.

Maybe I was surprised because I am having to start to do some thinking and engineering?

I think my opinion is increasingly that Claude 3.5 Sonnet is a bit like a Junior Developer - very good at writing code, but needs the logic and "what you're trying to do" hand-holding witha  code review to help through specifics like indexing etc.

Overall, painful - made much worse by trying to do it on Android.

TBH I still took way longer writing this up than I did solving the puzzle.
I may need to reduce how much I write if more complicated puzzles are going to need this many prompts.

## Solution

Neater than mine would have been.
Particularly like the reversible directions and use of reusable functions.

Overall, happy.
