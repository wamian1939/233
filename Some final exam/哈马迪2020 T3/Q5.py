# Final Exam - Question 5



def number_of_words_in_dictionary(word1, word2):
    '''
    Determines the number of words between two words "word1"
	and "word2" inclusive in the provided "dictionary.txt".

    "dictionary.txt" is stored in the working directory.
    Words in "dictionary.txt" are all uppercase.
    Words are case sensitive.


    >>> number_of_words_in_dictionary('company', 'company')
    Could not find company in dictionary.
    >>> number_of_words_in_dictionary('company', 'comparison')
    Could not find at least one of company and comparison in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'comparison')
    Could not find at least one of COMPANY and comparison in dictionary.
    >>> number_of_words_in_dictionary('company', 'COMPARISON')
    Could not find at least one of company and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPANY')
    COMPANY is in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPARISON')
    COMPARISON is in dictionary.
    >>> number_of_words_in_dictionary('COMPANY', 'COMPARISON')
    Found 14 words between COMPANY and COMPARISON in dictionary.
    >>> number_of_words_in_dictionary('COMPARISON', 'COMPANY')
    Found 14 words between COMPARISON and COMPANY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIOUSLY')
    Found 2 words between CONSCIOUS and CONSCIOUSLY in dictionary.
    >>> number_of_words_in_dictionary('CONSCIOUS', 'CONSCIENTIOUS')
    Found 3 words between CONSCIOUS and CONSCIENTIOUS in dictionary.
    '''

    with open('C:/Users/WMZ/Desktop/dictionarytxt.txt', 'r') as file:
        words = file.read().splitlines()

        if word1 not in words:
            if word2 not in words:
                if word1 == word2:
                    print(f"Could not find {word1} in dictionary.")
                else:
                    print(f"Could not find at least one of {word1} and {word2} in dictionary.")
            elif word2 in words:
                print(f"Could not find at least one of {word1} and {word2} in dictionary.")
        if word1 in words:
            if word2 not in words:
                print(f"Could not find at least one of {word1} and {word2} in dictionary.")

        if word1 in words:
            if word2 in words:
                index1 = words.index(word1)
                index2 = words.index(word2)
                if index1 == index2:
                    print(f'{word1} is in dictionary.')
                else:
                    start = min(index1, index2)
                    end = max(index1, index2)
                    count = end - start + 1
                    print(f'Found {count} words between {word1} and {word2} in dictionary.')

if __name__ == '__main__':
    import doctest

    doctest.testmod()

