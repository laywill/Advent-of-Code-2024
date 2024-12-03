# Day01 Write-Up

I think this challenge will need a diary to go along with solving the problem itself.

## Developing on Android

Initial impressions: this has come a really long way since I attempted this in 2023 and failed spectacularly.

In 2023 I tried running Python locally on my Android device, and struggled with basic operations like file IO.
By chosing to run everything in a GitHub Action that problem is neatly sidestepped.
I've also abandoned GitLab in favour of GitHub - my expectation is that a paid CoPilot subscription will integrate better this way, and I expect generally as a more popular platform the LLMs will produce more reasonable output.

I'm using a Samsung S23 UltraChIhavve the resolution maxed out at 1440p, and the text size set to "small". With glasses correcting my vision to 20:30 vision (better than average), this is a very text dense display with a good working area.
Again, last year suffered from trying to type non-dictionary terms a lot (int, elif,etc) which was painful in the extreme. Turning autocorrect off only served to highlight how good autocorrect and predictive typing is on mobile.
By using AI LLMs this year I am largely doing copy and paste, perhaps with basic note taking to edit my prompts.
This proved immediately easier and more suitable. 

The GitHub App is good generally.
Immediately I have total confidence this will work. 
It's not complete and I did have to fire up Chrome with [github.com](https://github.com) to do some admin tasks.


## LLM Choice

I'm starting with Claude Haiku for a few reasons:

1) It's a free LLM and I'm cheap.
2) It's a basic model, and I want to see if it can solve basic problems.
3) A whitepaper titled "AI for Software Engineering Teams" from [Engine Labs](https://engine labs.ai) suggests that Claude models are particularly widely used for LLM software generation at the moment. 

During the Day00 template generation, Claude seemed familiar with the Advent of Code in general, and took qquickly to creating a sensible template and repository setup.

## Problem

It's a trivial data parsing into lists, followed by list comprehension / comparison problem.

Usually these can be fiddly to deal with the parsing but trivial to write the functions to actually generate an answer.

## Prompt and Answers

### Part 1

I knew the basic shape of the solution so included a hint in my prompt.

As this is Day 1 there is a load of guff that also explains the AoC overall. That got chopped out using Google Keep as a basic text editor. 

The Prompt:

```plaintext
Ok, I've got the template for each day, and the GitHub Action running. We will now create `src/day01.py` using the template to Solve Day 1, Part 1.

I think this is a simple data parsing, sorting and comparing problem.

Here is the problem text:

--- Day 1: Historian Hysteria ---
The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months!

...

Everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:
````
```
3   4
4   3
2   5
1   3
3   9
3   3
```
````
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

In the example list above, the pairs and distances would be as follows:

The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
```

The LLM is surprisingly on it, with context drawn from earlier prompts, noting e.g. about Paet 2 coming later.

```
 I'll help you solve Day 1, Part 1. Based on the problem description, we need to:
1. Read two lists of numbers from the input file
2. Sort both lists
3. Calculate the distance between paired numbers
4. Sum these distances

Here's a solution:

...

Key points about the solution:

1. `read_input()` function:
   - Reads the input file
   - Converts each line to two integers
   - Creates separate lists for left and right numbers

2. `solve_part1()` function:
   - Sorts both input lists
   - Uses `zip()` to pair sorted lists
   - Calculates absolute difference between paired numbers
   - Sums these differences

3. Follows the template from our previous discussion
4. Handles the problem's requirements:
   - Sorts lists independently
   - Pairs smallest with smallest, etc.
   - Calculates distance between each pair
   - Sums total distance

The code will:
- Read input from `inputs/day01.txt`
- Sort the lists
- Calculate the total distance
- Print the solution

Note: Part 2 is left as a placeholder, as we haven't seen its requirements yet.

Would you like me to explain any part of the solution in more detail?
```


I copy-pasted the code, into a new file named as directed during the day00 template setup activity, using the GitHub app.

I checked the output of the GitHub Action, realised I'll have to manually type the answer as hold-to-select defaults to select all.

Bugger me... right answer strstraight away!


### Part 2

I got lazy and decided to throw it a more open ended Prompt. 

```
Smashed it - your solution worked and got the right answer first time. Now for Part 2.

Here is the puzzle text:
--- Part Two ---
Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3
For these example lists, here is the process of finding the similarity score:

The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
The fourth number, 1, also does not appear in the right list.
The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
The last number, 3, appears in the right list three times; the similarity score again increases by 9.
So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity score?
```

The response is again, generally excellent, with clear explanations, commented code, and cocognicence drawn from earlier prompts.


```
  I'll modify the existing solution to add Part 2 functionality:

...

Key changes for Part 2:

1. Imported `Counter` from `collections` to easily count occurrences

2. Updated `solve_part2()` function:
   - Uses `Counter` to count occurrences of numbers in the right list
   - Calculates similarity score by:
     * Iterating through left list numbers
     * Multiplying each number by its count in the right list
     * Summing these products

The solution follows the problem description exactly:
- Count how many times each left list number appears in the right list
- Multiply each left list number by its count
- Sum these products to get the similarity score

The code will:
- Read the same input from `inputs/day01.txt`
- Solve Part 1 as before
- Calculate the similarity score for Part 2
- Print both solutions

Would you like me to explain any part of the solution in more detail?
```

Again, bugger me if it wasn't right first time!

## Solution

Honestly, I'm happy.

Parsing the file into two lists: same approach I would take. I appreciate the use of a `map` rather than `for` loop - an optimisation I can't say I would have made, certainly not in a first pass.

Part 1 is almost verbatim what I was hoping for in my head.

Part 2 is definitely cleaner code than I would write. Mentally I was prepped for a `map` function to deduplicate, then a dictionary using the map values as keys, and a list comprehension to count instances of the keys. I didn't know about Counter, which achieves this as a 1 line call. Honestly, strong start!

Bonus: docstrings written and in-line comments.

I do feel that for clarity I maybe ought to label the code as AI generated somehow.