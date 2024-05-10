# COMP9021 24T1
# Quiz 6 *** Due Thursday Week 9 @ 9.00pm
#        *** Late penalty 10% per day
#        *** Not accepted after Sunday Week 9 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).
# Neighbours are only considered vertically or horizontally (not diagonally).
# Note that a shape with a single 1 is also a spike.

from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)

def count_spike(grid,x,y):
    count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < len(grid[0]) and 0 <= nx < len(grid) and grid[nx][ny] == 1:
            count += 1
    return count == 1

def dfs(grid,x,y,visited):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == 0 or visited[x][y]:
        return 0
    visited[x][y] = True
    spike_count = 1 if count_spike(grid, x, y) else 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dx, dy in directions:
        ny = y + dy
        nx = x + dx
        spike_count += dfs(grid, nx, ny,visited)
    return spike_count

def colour_shapes(grid):
    visited = [[False for _ in range(10)] for _ in range(10)]
    max_spike = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1 and not visited[i][j]:
                current_spike = dfs(grid, i, j, visited)
                max_spike = max(current_spike,max_spike)
    return max_spike


def max_number_of_spikes(nb_of_shapes):
    return nb_of_shapes

try:
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
nb_of_shapes = colour_shapes(grid)
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )