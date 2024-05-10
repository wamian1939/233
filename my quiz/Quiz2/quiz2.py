# COMP9021 24T1
# Quiz 2 *** Due Thursday Week 4 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 4 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


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

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
eight_code = f"{'0' * nb_of_leading_zeroes}{int(code):o}"
directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
grid = {(0, 0): True}
x, y = 0, 0
for digit in reversed(eight_code):
    dx, dy = directions[int(digit, 8)]
    x, y = x + dx, y + dy
    if (x, y) in grid:
        grid.pop((x, y))
    else:
        grid[(x, y)] = True
loop = False
if grid:
    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())
    loop = True
else:
    print(" ", end="")

if loop:
    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if grid.get((j, i), False):
                print(on, end='')
            else:
                print(off, end='')
        print()