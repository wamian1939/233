# A sequence of identical digits is collapsed to one digit
# in the returned integer.
#
# You can assume that the function is called with an integer
# as argument.


def collapse(number):
    '''
    >>> collapse(0)
    0
    >>> collapse(-0)
    0
    >>> collapse(9)
    9
    >>> collapse(-9)
    -9
    >>> collapse(12321)
    12321
    >>> collapse(-12321)
    -12321
    >>> collapse(-1111222232222111)
    -12321
    >>> collapse(1155523335551116111666)
    152351616
    >>> collapse(-900111212777394440300)
    -9012127394030
    '''
    # return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    numbers_list = list(str(number))
    result = [numbers_list[0]]
    for i in range(1,len(numbers_list)):
        if result[-1] != numbers_list[i]:
            result.append(numbers_list[i])
    print(''.join(result))


    # result = ''.join(numbers_set)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
