# Final Exam - Question 2

def filtered_sequence(L, n):
    '''
    Returns a list LL that keeps from L all elements e
    that are part of a sub-sequence of length at least n.

    All elements of the sub-sequence have the same value as e.

    You can assume that L is a list of valid integers.

    >>> filtered_sequence([], 2)
    []
    >>> filtered_sequence([7], 0)
    [7]
    >>> filtered_sequence([7], 1)
    [7]
    >>> filtered_sequence([7], 2)
    []
    >>> filtered_sequence([1, 3, 1, 2, 5, 6, 8, 2], 1)
    [1, 3, 1, 2, 5, 6, 8, 2]
    >>> filtered_sequence([1, 3, 3, 3, 2, 4, 4, 5, 6, 6, 6, 6], 2)
    [3, 3, 3, 4, 4, 6, 6, 6, 6]
    >>> filtered_sequence([7, 7, 7, 7, 2, 2, 7, 3, 4, 4, 4, 6, 5], 3)
    [7, 7, 7, 7, 4, 4, 4]
    >>> filtered_sequence([1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 6], 4)
    [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    '''

    if not L:
        return []
    result = []
    current = [L[0]]
    for i in range(1, len(L)):
        if current[-1] == L[i]:
            current.append(L[i])
        else:
            if len(current) >= n:
                result.extend(current)
            current = [L[i]]
    if len(current) >= n:
        result.extend(current)
    return result

    # INSERT YOUR CODE HERE


if __name__ == '__main__':
    import doctest

    doctest.testmod()
