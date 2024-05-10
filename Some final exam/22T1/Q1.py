# Will be tested only with number an integer.
#
# If number is positive, returns a positive integer.
# If number is negative, returns a negative integer.
#
# The digits of the returned integer are the digits of number
# ordered from largest to smallest.


def reorder(number):
    """
    >>> reorder(0)
    0
    >>> reorder(2)
    2
    >>> reorder(-33)
    -33
    >>> reorder(202)
    220
    >>> reorder(242242)
    442222
    >>> reorder(-3210123)
    -3322110
    >>> reorder(22659717106393887106)
    99887776665332211100
    """
    # return 0
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    if number >= 0:
        number_str = []
        for i in str(number):
            number_str.append(i)
        sorted_number = list(reversed(sorted(number_str)))
        result = ''.join(sorted_number)
        print(result)
    else:
        number_str = []
        for i in str(number):
            number_str.append(i)
        number_str.pop(0)
        sorted_number = list(reversed(sorted(number_str)))
        result ='-' + ''.join(sorted_number)
        print(result)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
