# Beginner Project 29: Sudoku Generator And Solver

**Time:** 5-7 hours  
**Difficulty:** Intermediate Beginner  
**Focus:** Puzzle generation, backtracking algorithms, constraint propagation, solver tracing, and puzzle validation

---

## Why This Project?

Building Sudoku generators and solvers requires implementing constraint satisfaction algorithms, understanding backtracking search, and designing efficient puzzle generation pipelines. Production puzzle systems must validate uniqueness, support difficulty levels, and trace solving steps for educational purposes.

This project teaches algorithm design and constraint solving where you can:

- generate valid Sudoku puzzles with guaranteed unique solutions,
- implement constraint propagation to reduce candidate values,
- apply backtracking search to solve puzzles efficiently,
- detect and score puzzle difficulty based on solving steps required,
- generate puzzles at various difficulty levels (easy, medium, hard, expert),
- trace and explain each solver step for educational purposes,
- validate puzzles against Sudoku rules,
- export generated puzzles and solutions to JSON format,
- handle edge cases (invalid inputs, unsolvable states) gracefully,
- and persist puzzle catalogs and solving histories to disk for analysis.

---

## More Projects

You can access this project and more in this separate repository:

[student-interview-prep](https://github.com/ShamShamsw/student-interview-prep.git)

---

## What You Will Build

You will build a Sudoku puzzle generator and solver that:

1. Generates valid Sudoku puzzles with exactly one solution.
2. Implements constraint propagation to efficiently narrow down candidate values.
3. Uses backtracking search to solve puzzles step-by-step.
4. Traces solver execution to record each deduction and guess.
5. Calculates puzzle difficulty based on solving techniques required.
6. Generates puzzles at configurable difficulty levels (easy to expert).
7. Validates all puzzles against standard Sudoku constraints.
8. Exports puzzles, solutions, and solver traces to JSON format.
9. Analyzes solve metrics (steps, iterations, guess count) for diagnostics.
10. Persists puzzle catalogs and solving sessions to disk for later review.

---

## Requirements

- Python 3.11+
- `numpy` (for efficient board manipulation and constraint tracking)

Install with:

```bash
pip install -r requirements.txt
```

---

## Example Session

```text
======================================================================
   SUDOKU GENERATOR AND SOLVER
======================================================================

Configuration:
   Generation mode:      Random with backtracking
   Difficulty level:     Medium
   Clue count target:    35-42
   Solution verification: Enabled
   Trace depth:          Full step-by-step
   Output format:        JSON

Startup:
   Data directory:       data/
   Outputs directory:    data/outputs/
   Puzzle catalog:       data/puzzles.json (loaded 0 puzzles)

---

Generating Sudoku Puzzle (Medium difficulty):
   [INIT]    Empty 9x9 board initialized
   [FILL]    Generating complete solution via backtracking
   [SOLVE]   Filled cells: 81/81
   [VERIFY]  Solution verified (valid)
   [REMOVE]  Removing clues to create puzzle
   [REMOVE]  Target clue count: 35-42
   
   Progress:
      Cells removed: 1   Candidates: 54   Solutions checked: 1
      Cells removed: 5   Candidates: 45   Solutions checked: 3
      Cells removed: 10  Candidates: 40   Solutions checked: 8
      Cells removed: 35  Candidates: 46   Solutions checked: 45

   [CHECK]   Puzzle has exactly 1 solution
   [DONE]    Puzzle generated successfully

   Generated Puzzle (35 clues):
   5 3 . | . 7 . | . . .
   6 . . | 1 9 5 | . . .
   . 9 8 | . . . | . 6 .
   ------+-------+------
   8 . . | . 6 . | . . 3
   4 . . | 8 . 3 | . . 1
   7 . . | . 2 . | . . 6
   ------+-------+------
   . 6 . | . . . | 2 8 .
   . . . | 4 1 9 | . . 5
   . . . | . 8 . | . 7 9

---

Solving Puzzle (Step-by-step):
   [START]   Puzzle loaded with 35 clues
   [INIT]    Initialized candidate sets for all cells
   
   Step 1:
      Technique:      Naked Single
      Cell:           (0, 4) = 7
      Reason:         Cell (0,4) has only 1 candidate: 7
      Eliminated:     Row 0: 1 candidate, Column 4: 2 candidates, Box 1: 1 candidate
      Remaining:      46/81 cells filled

   Step 2:
      Technique:      Hidden Single
      Row 1:          Cell (1, 1) = 2
      Reason:         Value 2 appears in only 1 cell in Row 1
      Eliminated:     Row 1: 1 candidate, Column 1: 2 candidates, Box 0: 2 candidates
      Remaining:      47/81 cells filled

   Step 3:
      Technique:      Hidden Single
      Column 2:       Cell (0, 2) = 1
      Reason:         Value 1 appears in only 1 cell in Column 2
      Eliminated:     Row 0: 1 candidate, Column 2: 1 candidate, Box 1: 1 candidate
      Remaining:      48/81 cells filled

   [... 33 more steps ...]

   Step 37:
      Technique:      Hidden Single
      Box 8:          Cell (8, 8) = 9
      Reason:         Value 9 appears in only 1 cell in Box 8
      Eliminated:     Row 8: 1 candidate, Column 8: 1 candidate, Box 8: 1 candidate
      Remaining:      81/81 cells filled

   [DONE]    Puzzle solved

Solving Statistics:
   Total steps:         37
   Naked Singles:       18
   Hidden Singles:      19
   Backtracking needed: No
   Solution Checks:     1
   Time elapsed:        0.047 seconds

Solution:
   5 3 4 | 6 7 8 | 9 1 2
   6 7 2 | 1 9 5 | 3 4 8
   1 9 8 | 3 4 2 | 5 6 7
   ------+-------+------
   8 5 9 | 7 6 1 | 4 2 3
   4 2 6 | 8 5 3 | 7 9 1
   7 1 3 | 9 2 4 | 8 5 6
   ------+-------+------
   9 6 1 | 5 3 7 | 2 8 4
   2 8 7 | 4 1 9 | 6 3 5
   3 4 5 | 2 8 6 | 1 7 9

Puzzle Metadata:
   Difficulty:       Medium
   Clue count:       35
   Solution count:   1 (unique)
   Min candidates:   1
   Max candidates:   7
   Avg candidates:   3.2

Artifacts saved:
   Generated puzzle:     data/outputs/puzzle_2024_03_16_001.json
   Solution trace:       data/outputs/trace_2024_03_16_001.json
   Puzzle catalog:       data/puzzles.json
```

