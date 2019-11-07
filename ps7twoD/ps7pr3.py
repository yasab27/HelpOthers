#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random


def count_neighbors(cellr, cellc, grid):
    """This function takes a location (row, column) in a grid of values and
       figures out how many of its neighbors (not including itself) are 
       alive (==1)
    """
    count = 0
    for k in range(cellr - 1, cellr + 2):
        for x in range(cellc - 1, cellc + 2):
            if (k == cellr) and (x == cellc):
                count += 0
            else:
                if (grid[k][x] == 1):
                    count += 1

    return count


def next_gen(grid):
    """This function creates and retursn a new 2-D list representing the
       next generation of cells.
    """
    new_grid = []
    height = len(grid)
    width = len(grid[0])
    new_grid = copy(grid)
    for r in range(1, height-1):
        for c in range(1, width-1):
            arrange = count_neighbors(r, c, grid)
            if arrange < 2:
                new_grid[r][c] = 0
            elif arrange == 2 and grid[r][c] == 1:
                new_grid[r][c] = 1
            elif arrange == 3 and grid[r][c] == 0:
                new_grid[r][c] = 1
            elif arrange > 3:
                new_grid[r][c] = 0

    return new_grid


def copy(grid):
    """This function creates a deep copy of a grid that has the same dimensions
       as the previous one. However, adjustments can be made for the new grid
       that do not affect values of the old grid. 
    """
    new_grid = []
    height = len(grid)
    width = len(grid[0])
    new_grid = create_grid(height, width)
    for r in range(height):
        for c in range(width):
            new_grid[r][c] = grid[r][c]

    return new_grid


def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []

    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid


def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')
        print()



def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid


def inner_grid(height, width):
    """This function creates a grid in which all outside numbers are 0 and 
    all inside are 1.
    """
    grid = create_grid(height, width)
    for r in range(1, height - 1):
        for c in range(1, width - 1):
            if r > 0 and r < height - 1:
                grid[r][c] = 1
    return grid


grid1 = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0]]

grid2 = next_gen(grid1)
print_grid(grid2)
print()
grid3 = next_gen(grid2)
print_grid(grid3)
