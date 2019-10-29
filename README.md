# sudoku-solver
Fast and simple command-line Sudoku solver.

# Usage

Command line:
```
cat examples/hardest.sudoku | ./sudokusolver.py
```

Python:
```
import gomokusolver

grid = ...
sudokusolver.solve(grid)
sudokusolver.print_grid(grid)
```
