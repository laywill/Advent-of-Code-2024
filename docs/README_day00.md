# Day00 - Setup, Template, Introduction 

The project README has hopefully explained what's going on: I'm in Australia on holiday during AoC this year. I only have my Android smartphone and any apps or web services I can access.

I haven't had a real chance to push LLMs coding ability, and understand prompt engineering for Software development, and this seems like a good opportunity. 

## What went wrong doing this last year

Last year I was in the Netherlands, Belgium and France during AoC and attempted to solve it by writing and running Python natively on my phone.
This was terrible.

Autocorrect did not like terms used in Python, and certainly didn't like variable names.
Python itself couldn't do file IO.

I've previously always had CI pipelines that will run all my code for me.

## How I'm fixing it this year

The plan is to use AI LLMs to do the coding.
I can write in English that autocorrect won't fight. Super.

I'll use GitHub Actions as a CI platform to run the code - I understand this well, and it makes more sense than trying to run it locally anyway.

## Setup

### Python Template 

I want my AI LLM to use a familiar feeling Template for each day.
Having this established in my conversation history should help ensure it generates code in a format that I'm expecting and is conducive to solving the AoC cleanly and effectively, with part 2 reusing or extending work from Part 1.


Initial Prompt:

```plaintext 
You are an expert Python programmer who will code solutions to the Advent of Code. There will be 25 puzzles, each with two parts: part 1 must be solved to unlock part 2. Part 1 and Part 2 use the same input data. I will supply an input to each file in a text file. The solution will need to read in this text file.
```

Response:

```plaintext 
 I'd be happy to help you solve the Advent of Code puzzles using Python! I'll create solutions that:
- Read input from a text file
- Solve both Part 1 and Part 2 of each puzzle
- Use efficient and clean Python code
- Handle the specific input requirements for each day's challenge

Would you like me to start by showing you a template for reading input files that we can use across different puzzles? This template will demonstrate how to read the input data and provide a basic structure for solving Advent of Code challenges.

Here's a general template I recommend:


<antArtifact identifier="aoc-solution-template" type="application/vnd.ant.code" language="python" title="Advent of Code Solution Template">
...
</antArtifact>

This template provides several key features:
1. Uses `pathlib` to handle file paths (works across different operating systems)
2. Reads input file and strips whitespace
3. Provides separate functions for Part 1 and Part 2
4. Includes a `main()` function to run both parts
5. Prints solutions for both parts

A few additional tips for Advent of Code:
- Always keep your input file (`input.txt`) in the same directory as your solution script
- The `read_input()` function can be modified to parse input differently for each puzzle
- Some puzzles might require converting input to integers, splitting in specific ways, etc.

Would you like me to elaborate on any part of this template, or are you ready to start with the first puzzle?
```


We're off, super. But what to do with this Template file... I'll ask Claude!
While we're at it, it is written to accept a single input file, and we will have one per day plus multiple source files.
See if it can handle that while we're here.


```
We're going to have 25 source files (one per day) and 25 text files with the input data in them. How should we organise a git repo? Do we need to update the template Python file as a result?
```

Response:


```plaintext 
 Great question! Here's a recommended project structure for an Advent of Code repository:

````
```
advent-of-code-2024/
│
├── src/
│   ├── day01.py
│   ├── day02.py
│   ├── ...
│   └── day25.py
│
├── inputs/
│   ├── day01.txt
│   ├── day02.txt
│   ├── ...
│   └── day25.txt
│
├── .gitignore
└── README.md
```
````

I'll update the template to reflect this structure:

<antArtifact identifier="aoc-solution-template" type="application/vnd.ant.code" language="python" title="Updated Advent of Code Solution Template">
...
</antArtifact>

I'll also suggest a `.gitignore` file:

<antArtifact identifier="gitignore" type="application/vnd.ant.code" language="gitignore" title="Gitignore for Advent of Code">
</antArtifact>

And a sample README:

<antArtifact identifier="readme" type="text/markdown" title="Advent of Code README">
...
</antArtifact>

Key changes and benefits:
1. Separated source code and input files
2. Automated day number extraction from filename
3. More flexible input reading method
4. Consistent naming convention
5. Gitignore to prevent accidental commits of sensitive data
6. README with setup instructions

Advantages of this approach:
- Scalable to all 25 days
- Easy to navigate
- Keeps inputs separate from code
- Allows easy running of individual day's solution
- Consistent file naming

Would you like me to elaborate on any part of this project structure?

```

The fix to the template wwas exactly what I wanted, but still no indication where to put it.
I opted to call it Day00.py

The gitignore file was fine, but worse than the template one provided by GitHub. Ignored.

The README was decent. I inserted my own sentences I'd written when creating the repo, but otherwise used it verbatim.


### GitHub Action

Prompt:
```
This is great. I can only run my Python using GitHub actions. I will need to inspect the GitHub Action outputs and/or artefacts to find the answers to each puzzle. What do we need to do to set this up? I want the pipeline to run every time the code changes.
```

Response:
```
 I'll help you set up a GitHub Actions workflow that will run your Advent of Code solutions automatically. Here's a comprehensive workflow configuration:

<antArtifact identifier="github-workflow" type="text/yaml" title="Advent of Code GitHub Actions Workflow">
...
</antArtifact>

I'll also create a helper script to make adding input files easier:

<antArtifact identifier="input-setup-script" type="application/vnd.ant.code" language="python" title="Input File Setup Script">
...
</antArtifact>

Let me explain the GitHub Actions workflow:

1. **Trigger Events**:
   - Runs on push to main branch
   - Runs on pull requests to main branch
   - Can be manually triggered

2. **Jobs**:
   - `solve-puzzles`: Runs all day solutions
     - Checks out the repository
     - Sets up Python 3.11
     - Runs all day scripts
     - Captures output in individual files
     - Uploads results as an artifact
     - Displays results in the workflow log

3. **Artifact**:
   - Results saved for 90 days
   - Can be downloaded from GitHub Actions page
   - Individual output files for each day

4. **Bonus Lint Job**:
   - Runs flake8 for code quality checks
   - Helps maintain code standards

To use this setup:

1. Place this workflow in `.github/workflows/aoc_solutions.yml`
2. The input setup script can be placed in `scripts/setup_input.py`

You can create input files easily:
```bash
python scripts/setup_input.py 1  # Creates inputs/day01.txt
```

To add an input file for a specific day:
1. Go to the Inputs tab in GitHub Actions
2. Download the input
3. Save it to the corresponding `inputs/dayXX.txt`

Benefits:
- Automatic running of all solutions
- Persistent artifact storage
- Code quality checks
- Easy input file management

Would you like me to elaborate on any part of this GitHub Actions setup?
```

Really nice that it included how to setup the actions, where to put the file, Flake8 included for free (not what I asked for so arguably a fail... but actually kinda handy).

The `setup_input.py` script threw me... it might be useful, but we're creating empty text files. This is kinda handy I guess, but a lot of script for the equivalent of `touch inputs/day00.txt`.
I cant use it anyway as I'm on Android... bit pointless and not what I asked for.

Notably the GitHub action only runs one file, and won't scale. It hasn't really picked up on the fact we need to scale to all 25 days. 

Prompt:
```
The GitHub actions run, but we need Run All Solutions to always store all the artefacts.
```

Response:
```
 I'll modify the workflow to ensure all artifacts are always stored, regardless of the job's outcome. Here's an updated version:

<antArtifact identifier="github-workflow" type="text/yaml" title="Advent of Code GitHub Actions Workflow with Always Upload Artifacts">
...
</antArtifact>

Key improvements:
1. Added `if: always()` to ensure jobs run even if previous steps fail
2. Added `continue-on-error: true` to the solution runner
3. Captures and reports errors for individual scripts
4. Ensures artifacts are uploaded even if some scripts fail
5. Added error handling to exit with a non-zero status if any script fails

The workflow now:
- Runs all scripts, even if some fail
- Captures output for each script
- Always uploads artifacts
- Provides comprehensive logging
- Allows manual investigation of failures

When you check the GitHub Actions run:
- You'll see individual script results
- Artifacts will always be available
- Failed scripts won't stop the entire workflow

Would you like me to explain any part of this updated workflow in more detail?
```

This did all work to be fair, but was irritating AF to access the artefacts, download, unzip (possible, using Samsung file browser!) and read.

Prompt:
```
Using artefacts is proving to be extremely difficult. We need to change the GitHub actions so it only outputs to terminal.
```

Response:
```
 I'll modify the GitHub Actions workflow to simplify output and just print to the terminal:

<antArtifact identifier="github-workflow" type="text/yaml" title="Simplified Advent of Code GitHub Actions Workflow">
...
</antArtifact>

Key changes:
1. Removed artifact generation
2. Simplified solution running
3. Prints output directly to terminal
4. Provides clear separation between day solutions
5. Maintains the linting job

The workflow now:
- Runs all scripts
- Prints output to the workflow log
- Allows direct viewing of results in GitHub Actions
- Keeps the linting check

Benefits:
- No complex artifact handling
- Easy to read results directly in the Actions tab
- Simple, straightforward execution

Would you like me to explain anything further about this simplified workflow?
```

This did what I wanted buacI had some issues with the day00.py file.

It was being picked up as a valid day to run, but had no input file.
The name was matching the pattern glob, when I dont really want it to etc.

I had to fiddle this a bit in the end to stop it failing the GitHub Action, and at this point I had just done the manual fixes before I thought to ask AI.


## Conclusion 

This took about an hour and a half all told, while laid in bed, and mostly with me fiddling trying to get my way around the apps.

Overall, still much faster than trying to do it by hand, and a really solid base to build on.