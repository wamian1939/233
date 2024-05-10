# COMP9021 24T1
# Quiz 4 *** Due Thursday Week 7 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 7 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a strictly positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):
    two_list = []
    for i in list_of_integers:
        two = ''
        while i > 0:
            a = i % 2
            two += str(a)
            i //= 2
        rev_two= two[::-1]
        two_list.append(rev_two)
    encode_str = []
    for single_str in two_list:
        duplicated_str = ''.join(char * 2 for char in single_str)
        encode_str.append(duplicated_str)
    combine = '0'.join(encode_str)
    encode_num = int(combine, 2)
    return encode_num


def decode(integer):
    two = ''
    while integer > 0:
        a = integer % 2
        two += str(a)
        integer //= 2
    integer_list = list(reversed(two))
    if len(integer_list) < 2:
        return None
    list_bi = []
    list_bi_in = []
    index = 0
    while index < len(integer_list):
        if integer_list[index] == '1' and integer_list[index + 1] != '1':
            return None
        if integer_list[-1] == '1' and integer_list[-2] == '0':
            return None

        if integer_list[index] == integer_list[index + 1]:
            list_bi_in.append(integer_list[index])
            index += 2
        else:
            list_bi.append(list_bi_in)
            list_bi_in = []
            index += 1
    if list_bi_in:
        list_bi.append(list_bi_in)
    decode_list = []
    for i in list_bi:
        two_string = "".join(i)
        decode_num = int(two_string, 2)
        decode_list.append(decode_num)
    return decode_list


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))