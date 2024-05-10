# COMP9021 24T1
# Quiz 2 Sample Solution

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

# We start from a position that is the unique position
on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()

try:
    # Check that the input is a non-strictly negative integer.
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0

# Count the number of leading zeroes.
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
# Convert the input to base 8.
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# Mapping the digits to the directions in the grid.
directions = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1),
              4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)
             }

# Check if the given coordinate should be on or off.
def switch_on_or_off(p):
    if p in lit_points:
        lit_points.remove(p)
    else:
        lit_points.add(p)

# Initialise the starting position to the original point.
p = [0, 0]
# The initial coordinate is switched on.
lit_points = {tuple(p)}
code = int(code)

# If the input is 0:
if not code:
    p = [0, 1]
    lit_points.add(tuple(p))

# While the input is not 0:
while code:
    # We map the the rightmost digit to the direction.
    h_move, v_move = directions[code % 8]
    p[0] += h_move
    p[1] += v_move

    # Switch on or off the coordinate.
    switch_on_or_off(tuple(p))
    code //= 8

# Do for the leadig zeroes.
for _ in range(nb_of_leading_zeroes):
    # move N
    p[1] += 1
    switch_on_or_off(tuple(p))

# Check if we need to print the grid.
if lit_points:

    # Find the range of the grid.
    min_x = min(p[0] for p in lit_points) - 1
    max_x = max(p[0] for p in lit_points)
    x_diff = max_x - min_x

    # Sort the coordinates in the grid.
    lit_points = sorted(lit_points, key=lambda p: (-p[1], p[0]))
    # Get starting coordinate. X should be leftmost. Y should be topmost.
    current_x, current_y = min_x, max(p[1] for p in lit_points)
    for (x, y) in lit_points:
        d = current_y - y

        # Print lines with all off points.
        if d:
            print(off * (max_x - current_x))
            for _ in range(d - 1):
                print(off * x_diff)
            current_x = min_x
        # Print off points with on points.
        print(off * (x - current_x - 1), on, sep = '', end = '')

        # Update the current coordinate.
        current_x = x
        current_y = y
    print(off * (max_x - current_x))