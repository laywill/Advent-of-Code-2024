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

## Prompt

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

## Solution

...TBC!