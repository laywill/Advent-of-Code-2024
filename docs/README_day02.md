# Day02 Write-Up 

## Developing on Android

Nothing major to report.

Now the Github actions are in place, and I've figured out how to use the GitHub app, it's singing along.

Kind of irritating that the GitHub app is designed for hotfixes with only one file edited per commit.
This is good practice though, so hardly disasterous.

Currently the actions are running in a few sexonds once picked up by a public runner. If we end up with some inefficient solutions this is going to get really slow really fast.

## LLM Choice

Claude Haiku, worked yesterday, so I probably won't change until it fails to generate a valid solution. 

## Problem

Another trivial problem at first glance needing llist iteration with some realtively simple validation functions.

My immediate gut feel was:
- parse into list of lists of ints
- validate rule one: two deep copies of each list, sort one and reverse sort the other, and compare to original.
- validate rule two: for each list of ints check if adjacent values are within range.

## Prompt and Answers

Im starting to think that for these easy problems there isnt much prompt engineering required.

### Part 1

I tried just shoving the whole problem in and asking it for a solution.

The Prompt:

```plaintext
Again - smashed it and it worked first time! 

Time to tackle the next puzzle:

--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
```

The response:

```
 I'll create a solution for Day 2, Part 1 that checks the safety of each report:

<antArtifact identifier="day02-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 2 Solution">
...
</antArtifact>

Key points about the solution:

1. `read_input()` function:
   - Reads the input file
   - Converts each line to a list of integers
   - Returns a list of reports

2. `is_safe_report()` function:
   - Checks two conditions for safety:
     a) All levels are increasing by 1-3
     b) All levels are decreasing by 1-3
   - Uses `all()` with list comprehensions to check adjacent levels
   - Returns `True` if either increasing or decreasing is valid

3. `solve_part1()` function:
   - Counts number of safe reports using `is_safe_report()`
   - Uses a generator expression with `sum()`

The solution handles the problem requirements:
- Reads multi-level reports
- Checks if levels are consistently increasing or decreasing
- Ensures adjacent levels differ by only 1-3
- Counts number of safe reports

Would you like me to explain any part of the solution in more detail?
```

The LLM has actually already optimised better than my gut feel by combining the all ascending check with the adjacent levels within range check.
It's probably a neater solution that I would have come up with.

Bonus: Right answer first time!

### Part 2

So now we can remove one element from.each list to try and make it valid.

My gut feel was to:
- Run the part 1 validation 
- If a list is invalid, generate N lists, each with one element removed
- Iterate through these lists to see if one is valid

Given Part 1 I'm expecting the LLM to do the same or present some neat optimisation I've missed.

The Prompt:

```plaintext
Great work - Part 1 worked first time. Now to tackle Part 2:

--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
```

The Response:

```plaintext
 I'll modify the existing solution to incorporate the Problem Dampener logic:

<antArtifact identifier="day02-solution" type="application/vnd.ant.code" language="python" title="Advent of Code Day 2 Solution Updated">
...
</antArtifact>

Key changes for Part 2:

1. Added a new function `is_safe_without_one_level()`:
   - First checks if the report is already safe
   - If not, tries removing each level one at a time
   - Checks if the reduced report becomes safe
   - Returns `True` if any single-level removal makes the report safe

2. Modified `solve_part2()`:
   - Uses the new `is_safe_without_one_level()` function
   - Counts reports that become safe with the Problem Dampener

The solution handles the new Part 2 requirements:
- Checks if the original report is safe
- If not, tries removing each level
- Checks if the reduced report becomes safe
- Counts the number of reports that can be made safe by removing one level

The code will:
- Read the input from `inputs/day02.txt`
- Solve Part 1 as before
- Apply the Problem Dampener logic for Part 2
- Print both solutions

Would you like me to explain any part of the solution in more detail?
```

Claude basically did as I hoped it would, with a few nice list compressions for improved readability. 

Answer was right first time!
Again, impressive!

## Solution

I'm impressed.
I feel a little hollow.

I'm impressed because the puzzle is so well written that it is a complete Prompt in and of itself. I don't need to do any real Prompt engineering to make it work. For nearly zero effort I've got an answer and a neat solution. 

I feel a little hollow because I have a group chat of friends who challenge ourselves to do AoC each year, providing peer support.
Part 2 caught several people out, especially with boundaries and details of list slicing.
It sounded like a fun puzzle.
I got relatively little satisfaction from punching it into Claude, though was obviously blown away at how good the solution is.

I think it's a different feeling because this is a hobby solving puzzles for the joy of solving puzzles.
If this was work, I'd love to be able to not get bogged down in syntax and instead focus on what the problem is and why I want to solve it.