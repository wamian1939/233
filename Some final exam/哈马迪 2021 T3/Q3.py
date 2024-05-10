'''
You might find the ord() function useful.
'''


def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of nothing but lowercase letters.

    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwrstuvabcde')
    'rstuv'
    '''
    if not word:
        return ''
    else:
        result = []
        cur_result = [word[0]]
        for i in range(1, len(word)):
            if ord(cur_result[-1]) + 1 == ord(word[i]):
                cur_result.append(word[i])
            else:
                if len(cur_result) > len(result):
                    result = cur_result
                cur_result = [word[i]]

        if len(cur_result) > len(result):
            result = cur_result
        result_str = ''.join(result)
    return result_str




if __name__ == '__main__':
    import doctest

    doctest.testmod()

