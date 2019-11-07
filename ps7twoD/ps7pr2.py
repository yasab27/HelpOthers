#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

import random

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
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line


