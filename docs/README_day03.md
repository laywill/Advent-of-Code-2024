# Day03 Write-Up 

## Developing on Android

Nothing major to report.

Still kind of slow and annoying. Still wouldn't write bulk code this way.

I've started writing up using a Windows laptop, purely because otherwise formatting everything on mobile is too painful.
Annoyingly all I want to do is add the quote marks on the front of everything, but I can't find a quick and easy tool available on mobile to do column insertion VIM / VSCode style.
I'm not counting this as cheating - the core challenge is still being done on Android.

## LLM Choice

I started with Claude Haiku, then had to restart in a new chat where I was given access to Claude 3.5 Sonnet.

## Problem

Another trivial problem at first glance needing sone Regex to find valid strings

My immediate gut feel was:
- parse
- Use [regex101.com](https://regex1co.com) to figure out the right RegEx to ignore / include characters
- Write a function to apply tthe regex

I expect part2 will be a change to what is a valid function.

## Prompt and Answers

My chat with Claude Haiku  reached the token limit or some other error so wouldn't accept new prompts so I had to start a new chat. I decided to write a generic primer Prompt that will allow me to use a new chat with any LLM:

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

Claude Haiku accepted this and confirmed it was ready to code.

Response:

> I am ready to help solve Advent of Code puzzles! I will:
> 
> 1. Use Python 3 and follow the provided template structure
> 2. Read input from files using the given read_input() function
> 3. Implement solutions for both Part 1 and Part 2 in their respective functions
> 4. Ensure code is well-documented and efficient
> 5. Handle input processing and error cases appropriately
> 
> Please provide the puzzle description and I'll help create a solution. Feel free to share either Part 1 initially, or both parts if you have them. I'll make sure to break down the problem and explain my implementation approach.

### Part 1

I thought it would be interesting to test my primer prompt by just shoving the whole problem in and asking it for a solution.

However, the problem was phrased using highlighting to demonstrate correct and incorrect parsing.
I decided to refactor this into explicit bullet points to make it absolutely clear for the LLM to parse. 

The Prompt:

> Here is Day 3 part 1:
> 
> --- Day 3: Mull It Over ---
> "Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.
> The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"
> The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!
> It seems like the goal of the program is just to multiply some numbers. It does that with instructions like `mul(X,Y)`, where `X` and `Y` are each 1-3 digit numbers. For instance, `mul(44,46)` multiplies `44` by `46` to get a result of `2024`. Similarly, `mul(123,4)` would multiply `123` by `4`.
> However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like `mul(4*, mul(6,9!, ?(12,34)`, or `mul ( 2 , 4 )` do nothing.
> For example, consider the following section of corrupted memory:
> `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`
> Only the following sections are real mul instructions:
> - `mul(2,4)`
> - `mul(5,5)`
> - `mul(11,8)`
> - `mul(8,5)`
> 
> Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
> Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

The response:

> I'll help solve this puzzle! We need to find all valid `mul(X,Y)` instructions in the input, where X and Y are 1-3 digit numbers, multiply them, and sum all the results.
> 
> <antArtifact identifier="day03-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 3 Solution">
> ...
> </antArtifact>
> 
> The solution uses regex to find valid multiplication instructions. Here's how it works:
> 
> 1. The regex pattern `r'mul\((\d{1,3}),(\d{1,3})\)'` matches:
>    - Exactly "mul" followed by an opening parenthesis
>    - First number (1-3 digits) captured in group 1
>    - A comma
>    - Second number (1-3 digits) captured in group 2
>    - A closing parenthesis
> 
> 2. For each line in the input:
>    - Find all matches of the pattern using `re.finditer()`
>    - For each match:
>      - Extract the numbers using `.group(1)` and `.group(2)`
>      - Convert them to integers
>      - Multiply them
>      - Add the result to the running total
> 
> 3. Return the final sum
> 
> The code will automatically ignore invalid instructions like:
> - `mul[3,7]` (wrong brackets)
> - `mul ( 2 , 4 )` (spaces)
> - `mul(4*` (invalid characters)
> - `?(12,34)` (wrong prefix)
> 
> You can run this with your input file placed in the appropriate directory structure. The solution will be printed to the console.
> 
> Would you like me to test this with any specific examples or make any modifications?

Claude has been potentially too good. I think, based on the puzzle we need to be exact and unforgiving, rejecting whitespace as invalid.

However, we got the right answer first time. So my reading of the puzzle was less correct than the LLM.

### Part 2

Similar challenge to what I expected.

- Slightly more challenging as now we need to track indexes of the RegEx matches and we need to handle more RegExs, and discount "invalid" matches.
- Actually trivial if you know the syntax - so seems ideal for an LLM but fiddly for a human.
- If I was doing this I'd need to probably google the syntax and need to do a bit of thinking about to not get lost with the do / don't functions.
- To make it easy to debug I would capture everything then process a list of instructions afterwards.

The Prompt:

> That worked. Now solve part 2:
> 
> --- Part Two ---
> As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.
> 
> There are two new instructions you'll need to handle:
> 
> The do() instruction enables future mul instructions.
> The don't() instruction disables future mul instructions.
> Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
> 
> For example:
> 
> xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
> This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.
> 
> This time, the sum of the results is 48 (24 + 85).
> 
> Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

The Response:

> I'll modify the solution to handle the conditional `do()` and `don't()` instructions that enable/disable multiplication operations.
> 
> > <antArtifact identifier="day03-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 3 Solution Updated">
> > ...
> > </antArtifact>
> 
> The Part 2 solution extends the previous code to handle the new conditional instructions. Here's how it works:
> 
> 1. Added new regex patterns to detect:
>    - `do()` instructions
>    - `don't()` instructions
>    - Kept the existing `mul(X,Y)` pattern
> 
> 2. For each line:
>    - Find all instructions (mul, do, don't) and their positions in the line
>    - Store them in a list with their type and position
>    - For mul instructions, also store the numbers to multiply
> 
> 3. Sort all instructions by their position to process them in order
> 
> 4. Process instructions sequentially:
>    - Start with multiplications enabled (per puzzle rules)
>    - When we hit a `do()`, enable multiplications
>    - When we hit a `don't()`, disable multiplications
>    - When we hit a `mul()`, only add its result to the total if multiplications are currently enabled
> 
> The solution handles the example case correctly:
> ```
> xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))
> ```
> Only `mul(2,4)` and `mul(8,5)` are counted because:
> - `mul(2,4)` is processed while enabled (default state)
> - `don't()` disables multiplications
> - `mul(5,5)` and `mul(11,8)` are ignored (disabled)
> - `do()` re-enables multiplications
> - `mul(8,5)` is processed while enabled
> 
> Would you like me to test this with any specific examples or make any modifications?

For the first time, this didn't work straight out the box.

I thought we might as wel take the opportunity to setup PyTest for inevitably some more difficult problems later.

The prompt:

> We need to add tests to debug this using PyTest. My repository is structured like this:
> 
> ```
> advent-of-code-2024/
> │
> ├── src/
> │   ├── day01.py
> │   ├── day02.py
> │   ├── ...
> │   └── day25.py
> │
> ├── inputs/
> │   ├── day01.txt
> │   ├── day02.txt
> │   ├── ...
> │   └── day25.txt
> │
> ├── tests/
> │   ├── __init__.py
> │   ├── test_day01.py
> │   ├── test_day02.py
> │   ├── ...
> │   └── test_day25.py
> │
> ├── .gitignore
> └── README.md
> ```
> 
> Add test cases using only the example input and correct output I provided previously.

The Response:

> I'll create a test file for Day 3 using PyTest and the example cases from both parts.
> 
> > <antArtifact identifier="day03-tests" type="application/vnd.ant.code" language="python" title="Advent of Code Day 3 Tests">
> > ...
> > </antArtifact>
> 
> This test file (`tests/test_day03.py`) includes:
> 
> 1. `test_part1_example`: Tests Part 1 with the exact example from the problem description, expecting a sum of 161
> 
> 2. `test_part2_example`: Tests Part 2 with the exact example from the problem description, expecting a sum of 48
> 
> 3. `test_multiple_lines`: Additional test to verify both functions handle multiple lines correctly
> 
> 4. `test_empty_input`: Edge case test to ensure both functions handle empty input gracefully
> 
> The tests can be run using:
> ```bash
> pytest tests/test_day03.py -v
> ```
> 
> Or to run all tests in the project:
> ```bash
> pytest tests/ -v
> ```
> 
> If any test fails, PyTest will show:
> - The actual vs expected values
> - The line where the assertion failed
> - A detailed traceback
> 
> Would you like me to add any additional test cases or make any modifications to the existing ones?

Genuinely quite pleased. This includes the test cases I specified, plus a couple of other obvious cases like an empty string and a multiline string - this actually was jolly helpful in spotting the problem with the solution.

More pressingly, we needed a way to run the tests and see if they worked.

> I need to update my GitHub workflow to run Pytest. My repository is structured like this:
> 
> ```
> advent-of-code-2024/
> │
> ├── src/
> │   ├── day01.py
> │   ├── day02.py
> │   ├── ...
> │   └── day25.py
> │
> ├── inputs/
> │   ├── day01.txt
> │   ├── day02.txt
> │   ├── ...
> │   └── day25.txt
> │
> ├── tests/
> │   ├── __init__.py
> │   ├── test_day01.py
> │   ├── test_day02.py
> │   ├── ...
> │   └── test_day25.py
> │
> ├── .gitignore
> └── README.md
> ```
> 
> My current GitHub workflow looks like this:
> 
> ```
> name: Advent of Code Solutions
> 
> on:
>   push:
>     branches: [ "main" ]
>   pull_request:
>     branches: [ "main" ]
>   workflow_dispatch:  # Allow manual trigger
> 
> jobs:
>   solve-puzzles:
>     runs-on: ubuntu-latest
>     
>     steps:
>     - name: Checkout repository
>       uses: actions/checkout@v4
>     
>     - name: Set up Python
>       uses: actions/setup-python@v4
>       with:
>         python-version: '3.11'
>     
>     - name: Run All Day Solutions
>       run: |
>         # Loop through all day solutions
>         for day_script in src/day*.py; do
>           if [ -f "$day_script" ]; then
>             day=$(basename "$day_script" .py)
>             echo "=== Running $day ==="
>             python "$day_script"
>             echo ""  # Add a blank line between solutions
>           fi
>         done
> 
>   lint-and-test:
>     runs-on: ubuntu-latest
>     steps:
>     - name: Checkout repository
>       uses: actions/checkout@v4
>     
>     - name: Set up Python
>       uses: actions/setup-python@v4
>       with:
>         python-version: '3.11'
>     
>     - name: Install dependencies
>       run: |
>         python -m pip install --upgrade pip
>         pip install flake8 pytest
>     
>     - name: Lint with flake8
>       run: |
>         flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
>         flake8 src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
> ```
> 
> Update my Github workflow.

The response:

> I'll help you update the GitHub workflow to include PyTest execution. The workflow needs to install pytest and run the tests after linting.
> 
> > <antArtifact identifier="github-workflow" type="text/yaml" title="Advent of Code GitHub Actions Workflow">
> > ...
> > </antArtifact>
> 
> Key changes made:
> 
> 1. Added a new step "Run tests with pytest" after the linting step
> 2. Set up PYTHONPATH to include the src directory, which is necessary for pytest to import modules from src/
> 3. Running pytest with the -v flag for verbose output to show all test results
> 
> The workflow will now:
> 1. Check out the code
> 2. Set up Python
> 3. Install dependencies (including pytest)
> 4. Run flake8 for linting
> 5. Run all pytest tests in the tests/ directory
> 
> The tests will fail the workflow if any test fails, which is the desired behavior for CI/CD.
> 
> You can put this file in your repository at `.github/workflows/python-app.yml` (or whatever your workflow file is named).
> 
> To test locally before pushing, you can run:
> ```bash
> PYTHONPATH=$PYTHONPATH:$(pwd) pytest tests/ -v
> ```
> 
> Would you like me to add any additional features to the workflow, such as:
> - Test coverage reporting
> - Caching of pip dependencies
> - Parallel test execution
> - Test result reporting
> - Specific pytest configurations?

I noticed that one test was failing, and for the second time the LLM had made a mistake - it had calculated the wrong number as the answer - though this was totally trivial to check with a calculator and correct:

> I think the test_multiple_lines() test is expecting the wrong answer. I think the right answer is 46.
> 
> Update just that test case.

The Response:

> > <antArtifact identifier="day03--updated" type="application/vnd.ant.code" language="python" title="Advent of Code Day 3 Tests Updated">
> > ...
> > </antArtifact>
> 
> I've updated the test_multiple_lines() function to:
> 
> Fix the expected value from 47 to 46
> Added a comment showing the detailed calculation: 24 + 33 + 55 + 22 = 8 + 9 + 25 + 4 = 46
> Updated both assertions to expect 46 instead of 47
> 
> The rest of the test file remains unchanged. Would you like me to add any additional test cases or make any other modifications?

I was being supremely lazy and so asked my another kind of LLM for an answer - my group chat with other friends completing the AoC if they had any tips for "gotchas" in Day 3 Part 2.

[@enygma999](https://github.com/enygma999) mentioned about the multiple lines test case working, but needing to test that the `do()` and `don't()` logic preserves accross multiple lines.

Prompt:

> Good job - all the tests pass, but our part2() answer is wrong.
> 
> I wonder if the new lines are causing us problems. Would we be better to strip out all newline characters right at the start and treat the input as one long line?

Reponse:

> Yes, that's a good insight! For part 2, the do/don't state should persist across lines, so treating the input as one long line would be more appropriate. Let's modify the solution.
> 
> > <antArtifact identifier="day03-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 3 Solution Updated">
> > ...
> > </antArtifact>
> 
> Key changes made:
> 1. In both `solve_part1` and `solve_part2`, immediately join all input lines into a single string using `''.join(input_data)`
> 2. Process all instructions in sequence across the entire input, maintaining a single `enabled` state
> 3. All regex operations now work on the combined input string instead of line by line
> 
> This change means:
> - The do/don't state will properly persist across what were previously line boundaries
> - All instructions are processed in the correct order regardless of line breaks
> - The solution should now handle multi-line inputs correctly while maintaining the proper state
> 
> The tests should still pass, but the part 2 solution should now give the correct answer for the full input. Would you like me to add any additional test cases to verify the behavior with multi-line inputs that include do/don't instructions?

This generated the correct part 2 solution.

So, look, on the one hand, it's a bit disappointing that the LLM has started to stumble on only Day 3 - this suggests I'm in for a slog.

On the other hand, the writeup has taken more time that I spent actually dealing with the code, and frankly I've had to do almost no real thinking at all so far and this has been really easy.

## Solution

The solutions are starting to show a trend of being reasonably well optimised, definitely well documented, but most importantly: working!
