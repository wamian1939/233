# COMP9021 24T1
# Quiz 3 *** Due Thursday Week 5 @ 9.00pm
#        *** Late penalty 5% per day
#        *** Not accepted after Sunday Week 5 @ 9.00pm

# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends and
#   around parentheses and commas, is a valid word.


import sys


def is_symbol(s):
    if s == ' ':
        return False
    for letter in s:
        if letter.isalpha() or letter == '_':
            continue
        else:
            return False
    return True


def is_valid(word, arity, is_recursive=False):
    if arity == 0:
        return is_symbol(word)

    if arity > 0 and not is_recursive:
        if '(' not in word or ')' not in word:
            return False

    if '(' in word and ')' in word and word.find('(') < word.find(')'):
        split_index = word.find('(')
        if split_index == -1:
            return False

        symbol = word[:split_index].strip()
        if not is_symbol(symbol):
            return False

        w_str = word[split_index:]
        if w_str[-1] != ')':
            return False

        w_str_without_parentheses = w_str[1:-1]
        parts = []
        current_part = []
        parentheses_level = 0

        for char in w_str_without_parentheses:
            if char == '(':
                parentheses_level += 1
            elif char == ')':
                parentheses_level -= 1

            if char == ',' and parentheses_level == 0:
                parts.append(''.join(current_part).strip())
                current_part = []
            else:
                current_part.append(char)

        parts.append(''.join(current_part).strip())

        if len(parts) != arity:
            return False
    else:
        if word.isalpha():
            return True
        else:
            return False

    return all(is_valid(part, arity, is_recursive=True) for part in parts)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
