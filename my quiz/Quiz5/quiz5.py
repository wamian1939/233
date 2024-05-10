# COMP9021 24T1
# Quiz 5 *** Due Thursday Week 8 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 8 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines moved to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines moved to the right by one position, e.g.
#      111
#       111
#        111
#         111
# The size is the number of 1s in the parallelogram. In the above examples, the size is 12.

from random import seed, randrange
import sys

dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def findmax(count):
    return max((min(count[i:j + 1]) * (j - i + 1) for i in range(len(count)) for j in range(i + 1, len(count))),
               default=0)


def size_of_largest_parallelogram():
    for i in range(dim):
        for j in range(dim):
            rectangle_size = find_square_max_size(grid)
            left_parallelogram_size = find_left_parallelogram_max_size(grid)
            right_parallelogram_size = find_right_parallelogram_max_size(grid)
            largest_size = max(rectangle_size, left_parallelogram_size, right_parallelogram_size)
    return largest_size


def find_square_max_size(grid):
    grid_plus = [[0] + row + [0] for row in grid]
    grid_add = [[0] * 12] + grid_plus + [[0] * 12]
    largest = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if grid_add[i][j] and grid_add[i][j + 1] and grid_add[i + 1][j] and grid_add[i + 1][j + 1]:
                count = [2]
                y_down = i
                x_right = j + 2
                while grid_add[y_down][x_right] == 1:
                    count[0] += 1
                    x_right = x_right + 1
                y_down = y_down + 1
                while grid_add[y_down][j] and grid_add[y_down][j + 1]:
                    count.append(2)
                    x_right = j + 2
                    while grid_add[y_down][x_right]:
                        count[-1] += 1
                        x_right += 1
                    y_down += 1
                current_size = findmax(count)
                largest = max(largest, current_size)
    return largest


def find_right_parallelogram_max_size(grid):
    grid_plus = [[0] + row + [0] for row in grid]
    grid_add = [[0] * 12] + grid_plus + [[0] * 12]
    largest = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if grid_add[i][j] and grid_add[i][j + 1] and grid_add[i + 1][j + 1] and grid_add[i + 1][i + 2]:
                count = [2]
                y_down, x_right = i, j + 2
                while grid_add[y_down][x_right] == 1:
                    count[0] += 1
                    x_right = x_right + 1
                y_down = y_down + 1
                x_right = j
                while grid_add[y_down][x_right - 1] and grid_add[y_down][x_right]:
                    count.append(2)
                    x_right_extra = x_right + 1
                    while grid_add[y_down][x_right_extra]:
                        count[-1] += 1
                        x_right_extra += 1
                    y_down += 1
                    x_right -= 1
                current_size = findmax(count)
                largest = max(largest, current_size)
    return largest


def find_left_parallelogram_max_size(grid):
    grid_plus = [[0] + row + [0] for row in grid]
    grid_add = [[0] * 12] + grid_plus + [[0] * 12]
    largest = 0
    for i in range(1, 11):
        for j in range(1, 11):
            if grid_add[i][j] == 1 and grid_add[i][j + 1] == 1 and grid_add[i + 1][j - 1] and grid_add[i + 1][j]:
                count = [2]
                y_down = i
                x_right = j + 2
                while grid_add[y_down][x_right] == 1:
                    count[0] += 1
                    x_right = x_right + 1
                y_down = y_down + 1
                x_right = j
                while grid_add[y_down][x_right - 1] and grid_add[y_down][x_right]:
                    count.append(2)
                    x_right_extra = x_right + 1
                    while grid_add[y_down][x_right_extra]:
                        count[-1] += 1
                        x_right_extra += 1
                    y_down += 1
                    x_right -= 1
                current_size = findmax(count)
                largest = max(largest, current_size)
    return largest


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
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
          )
else:
    print('There is no parallelogram with horizontal sides.')