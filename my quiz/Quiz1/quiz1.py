# COMP9021 24T1
# Quiz 1 *** Due Thursday Week 3 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 3 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
set1 = set()
for start_key in mapping:
    if start_key in set1:
        continue

    current_cycle = []
    current_key = start_key

    while current_key in mapping and current_key not in set1:
        current_cycle.append(current_key)
        set1.add(current_key)
        current_key = mapping[current_key]

    if current_key in current_cycle:
        index = current_cycle.index(current_key)
        cycle = current_cycle[index:]
        min_index = cycle.index(min(cycle))
        cycles.append(cycle[min_index:] + cycle[:min_index])


def takefirst(cycle):
    return cycle[0]


cycles.sort(key=takefirst)

reversed_dic = {}
for old_key in mapping.keys():
    new_key = mapping[old_key]
    if new_key in reversed_dic:
        reversed_dic[new_key].append(old_key)
    else:
        reversed_dic[new_key] = [old_key]

length_dic = {}

for n_keys, o_keys in reversed_dic.items():
    lenght = len(o_keys)
    if lenght not in length_dic:
        length_dic[lenght] = {}
    if n_keys not in length_dic[lenght]:
        length_dic[lenght][n_keys] = []

    length_dic[lenght][n_keys].extend(o_keys)
sorted_key = sorted(length_dic.keys())
reversed_dict_per_length = {lenght: length_dic[lenght] for lenght in sorted_key}

print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)
