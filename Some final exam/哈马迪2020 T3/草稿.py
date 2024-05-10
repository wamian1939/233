from random import seed, randint
import sys


def f(L):
    '''
    >>> L = []
    >>> f(L)
    -1
    >>> L = [1,2,3,4]
    >>> f(L)
    -1
    >>> L = [12,34]
    >>> f(L)
    -1
    >>> L = [121]
    >>> f(L)
    1.0
    >>> L = [123,234,235]
    >>> f(L)
    2.5
    '''
    # Insert your code here
    if not L:
        return  -1
    def isp(n):
        return str(n) == str(n)[::-1]

    if all(isp(num) for num in L):
        average = sum(L) / len(L)
        return average / 2
    else:
        return -1 

if __name__ == '__main__':
    import doctest

    doctest.testmod()

