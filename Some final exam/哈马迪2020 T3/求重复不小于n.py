# 求重复的不小于n的数字的列表


from random import seed, randint
import sys


def f(L, n):
    '''
    >>> L = []
    >>> f(L,2)
    []
    >>> L = [1,2,3,4]
    >>> f(L,5)
    []
    >>> L = [12,34]
    >>> f(L,8)
    []
    >>> L = [121]
    >>> f(L,10)
    []
    >>> L = [2,3,4,5,9,8,7,6,5,3]
    >>> f(L,2)
    [3, 5]
    >>> L = [3,3,3,3,3]
    >>> f(L,3)
    [3]
    '''
    # Insert your code here
    if not L:
        return []

    if L:
        l_set = set(L)
        result = []
        for i in l_set:
            if L.count(i) >= n:
                result.append(i)
        return result




if __name__ == '__main__':
    import doctest

    doctest.testmod()
