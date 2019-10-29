#!/usr/bin/python3

import os
import sys


def _parse_sudoku():
    grid = []
    for line in sys.stdin:
        row = []
        for char in line:
            if char == '-':
                row.append(0)
            elif char == '\n':
                continue
            else:
                row.append(int(char))
        assert len(row) == 9
        grid.append(row)
    assert len(grid) == 9
    return grid


_MAX_INDEX = 81


def _coords(index):
    return index // 9, index % 9


def _get_index(grid, index):
    row, col = _coords(index)
    return grid[row][col]


def _top_left_quad(row, col):
    return row - row % 3, col - col % 3


def _good(grid, row, col, n):
    for i in range(9):
        if i != row and grid[i][col] == n:
            return False
        if i != col and grid[row][i] == n:
            return False
        trow, tcol = _top_left_quad(row, col)
        for dy in range(3):
            for dx in range(3):
                y = trow + dy
                x = tcol + dx
                if y != row and x != col and grid[y][x] == n:
                    return False
    return True


def _possible_moves(grid, index):
    row, col = _coords(index)
    result = []
    for n in range(1, 9 + 1):
        if _good(grid, row, col, n):
            result.append(n)
    return result


def _find_unsolve_square(grid):
    best_index = None
    best_moves = None
    best_moves_count = 10
    for index in range(_MAX_INDEX):
        if _get_index(grid, index) != 0:
            continue
        index_moves = _possible_moves(grid, index)
        index_moves_count = len(index_moves)
        if index_moves_count < best_moves_count:
            best_index = index
            best_moves = index_moves
            best_moves_count = index_moves_count
            if best_moves_count == 1:
                break
    return best_index, best_moves


def solve(grid):
    index, moves = _find_unsolve_square(grid)
    if index is None:
        return True
    row, col = _coords(index)
    for n in moves:
        if _good(grid, row, col, n):
            grid[row][col] = n
            if solve(grid):
                return True
            grid[row][col] = 0
    return False
        

def print_grid(grid):
    print(".", end="")
    for c in range(9):
        print("===.", end="")
    print()
    for r in range(9):
        print("|", end="")
        for c in range(9):
            print(
                " {} ".format(" " if grid[r][c] == 0 else str(grid[r][c])),
                end=("|" if c % 3 == 2 else ":")
            )
        print()
        print(".", end="")
        for c in range(9):
            print("===" if r % 3 == 2 else "---", end=".")
        print()
    

if __name__ == "__main__":
    grid = _parse_sudoku()
    print_grid(grid)
    print(solve(grid))
    print_grid(grid)
