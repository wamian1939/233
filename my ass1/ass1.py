import sys,time
time.sleep(0.1)

input_string = input('How can I help you? ')
intput_string = input_string.strip()
# if len(input_string) <= 14:
#     print('I don\'t get what you want, sorry mate!')
#     sys.exit()

if input_string.split()[0] != 'Please' or input_string.split()[1] != 'convert' or len(input_string.split()) < 3 or len(
        input_string.split()) > 5 or len(input_string) <= 14:
    print('I don\'t get what you want, sorry mate!')
    sys.exit()


def continue_four(string):
    for i in range(len(string) - 3):
        if string[i] == string[i + 1] == string[i + 2] == string[i + 3]:
            return True
    return False


# first-----------------------------------------------------------------------------------------------------------------
if len(intput_string.split()) == 3:
    cot = intput_string.split()[2]
    if cot.isdigit():
        int_cot = int(cot)


    def roman_to_ara(roman):
        if continue_four(roman):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            if not is_valid_roman(roman, roman_map):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            ara = 0
            previous = 0
            for num in reversed(roman):
                if roman_map[num] < previous:
                    ara -= roman_map[num]
                else:
                    ara += roman_map[num]
                previous = roman_map[num]
            return ara


    def is_valid_roman(roman, roman_map):
        valid_symbols = set(roman_map.keys())
        for i, c in enumerate(roman):
            if c not in valid_symbols:
                return False
            if i > 0 and roman_map[roman[i - 1]] < roman_map[c]:
                if i == 1 or roman_map[roman[i - 2]] < roman_map[c]:
                    return False
        return True


    def ara_to_raman(ara):
        ara_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        roman = ''
        for value, num in ara_map:
            while ara >= value:
                ara -= value
                roman += num
        return roman


    if cot.isdigit() and cot[0] != '0' and 4000 > int(cot) > 0:
        print('Sure! It is ' + str(ara_to_raman(int_cot)))
        sys.exit()
    elif cot.isalpha():
        print('Sure! It is ' + str(roman_to_ara(cot)))
        sys.exit()
    else:
        print("Hey, ask me something that's not impossible to do!")


# Second----------------------------------------------------------------------------------------------------------------
# def second_check(input_s:str):
#     if len(input_s) < 4:
#         return
#     else:
#         using = input_s.split()[3]
#         if using != 'using':
#             print("I don't get what you want, sorry mate!")
#             if len(input_s) != len(set(input_s)):
#                 print("Hey, ask me something that's not impossible to do!")
#                 for i in list(input_s.split()[2]):
#                     if all(item in list(input_s.split()[4]) for item in list(input_s.split()[2])):
#                         print("Hey, ask me something that's not impossible to do!")
#     return True
def find(string):
    if len(string) != len(set(string)):
        return True
    return False


if len(intput_string.split()) == 5:
    if intput_string.split()[3] != 'using':
        print("I don't get what you want, sorry mate!")
        sys.exit()
    elif intput_string.split()[4].isalpha() == False or find(intput_string.split()[4]):
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()


    def cus_roman_to_ara(roman, symbol_string):
        symbol_values = {}
        base_value = 1

        for i, symbol in enumerate(reversed(symbol_string)):
            symbol_values[symbol] = base_value

            if i % 2 == 0:
                base_value *= 5
            else:
                base_value *= 2

        if continue_four(roman):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        else:
            if not is_valid_roman(roman, symbol_values):
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()

        arabic = 0
        previous_value = 0
        for symbol in reversed(roman):
            value = symbol_values.get(symbol, 0)
            if value < previous_value:
                arabic -= value
            else:
                arabic += value
            previous_value = value
        return arabic


    def is_valid_roman(roman, roman_map):
        valid_symbols = set(roman_map.keys())
        x = []
        for symbol, value in roman_map.items():
            x.append(symbol)
        x = x[1:len(x):2]
        five_multiples = set(x)

        consecutive_five_multiples_count = 0
        last_five_multiple = ''

        for i, c in enumerate(roman):
            if c not in valid_symbols:
                return False

            if c in five_multiples:
                if c == last_five_multiple:
                    consecutive_five_multiples_count += 1
                    if consecutive_five_multiples_count >= 3:
                        return False
                else:
                    consecutive_five_multiples_count = 1
                    last_five_multiple = c
            else:
                consecutive_five_multiples_count = 0
                last_five_multiple = ''

            if i > 0 and roman_map[roman[i - 1]] < roman_map[c]:
                if roman_map[roman[i - 1]] * 10 < roman_map[c] or i > 1 and roman_map[roman[i - 2]] < roman_map[c]:
                    return False

        return True


    def cus_ara_to_roman(ara, symbol_string):
        base_value = 1
        map = []
        rev_string = list(reversed(symbol_string))
        for i, symbol in enumerate(rev_string):
            map.append((base_value, symbol))
            if i % 2 == 0:
                base_value *= 5
            else:
                base_value *= 2

        for i in range(1, len(rev_string), 2):
            combine_value = map[i][0] - map[i - 1][0]
            combine_symbol = rev_string[i - 1] + rev_string[i]
            map.append((combine_value, combine_symbol))

        for i in range(2, len(rev_string), 2):
            combine_value = map[i][0] - map[i - 2][0]
            combine_symbol = rev_string[i - 2] + rev_string[i]
            map.append((combine_value, combine_symbol))

        map.sort(key=lambda x: x[0], reverse=True)

        roman = ''
        for value, symbol in map:
            while ara >= value:
                ara -= value
                roman += symbol
        return roman


    cot = intput_string.split()[2]
    if cot.isdigit():
        int_cot = int(cot)
    cus_symbol = intput_string.split()[4]
    if cot.isdigit():
        print("Sure! It is " + str(cus_ara_to_roman(int_cot, cus_symbol)))
    elif cot.isalpha():
        print("Sure! It is " + str(cus_roman_to_ara(cot, cus_symbol)))
    else:
        print("Hey, ask me something that's not impossible to do!")


# 3
def cus_roman_to_ara(roman, symbol_string):
    symbol_values = []
    base_value = 1

    for i, symbol in enumerate(reversed(symbol_string)):
        symbol_values.append((symbol, base_value))

        if i % 2 == 0:
            base_value *= 5
        else:
            base_value *= 2

    if continue_four(roman):
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()
    if not is_valid_roman(roman, symbol_values):
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()

    arabic = 0
    previous_value = 0
    for symbol in reversed(roman):
        value = next((val for sym, val in symbol_values if sym == symbol), 0)
        if value < previous_value:
            arabic -= value
        else:
            arabic += value
        previous_value = value
    return arabic


def is_valid_roman(roman, roman_map):
    roman_keys = [symbol for symbol, value in roman_map]
    valid_symbols = roman_keys
    x = []
    for symbol, value in roman_map:
        x.append(symbol)
    x = x[1:len(x):2]
    five_multiples = set(x)

    consecutive_five_multiples_count = 0
    last_five_multiple = ''

    for i, c in enumerate(roman):
        if c not in valid_symbols:
            return False
        if c in five_multiples:
            if c == last_five_multiple:
                consecutive_five_multiples_count += 1
                if consecutive_five_multiples_count >= 3:
                    return False
            else:
                consecutive_five_multiples_count = 1
                last_five_multiple = c
        else:
            consecutive_five_multiples_count = 0
            last_five_multiple = ''
        for i, c in enumerate(roman):
            if i > 0:
                prev_value = next((value for sym, value in roman_map if sym == roman[i - 1]), 0)
                curr_value = next((value for sym, value in roman_map if sym == c), 0)
                if prev_value <= curr_value:
                    if prev_value * 10 < curr_value:
                        return False
                    if i > 1:
                        two_prev_value = next((value for sym, value in roman_map if sym == roman[i - 2]), 0)
                        if two_prev_value < curr_value:
                            return False
    return True


def find_one(w, list):
    count = 0
    for e in list:
        if w == e:
            count += 1
    return count == 1


if len(intput_string.split()) == 4:
    if intput_string.split()[3] != 'minimally':
        print("I don't get what you want, sorry mate!")
        sys.exit()
    if intput_string.split()[2].isalpha():
        pass
    else:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    cot = intput_string.split()[2]
    alp = []
    for i in range(-1, -len(cot) - 1, -1):
        if cot[i] not in alp:
            alp.append(cot[i])
        else:
            index = alp.index(cot[i])

            if cot[i] != cot[i + 1]:
                if i + 2 >= -len(cot) and cot[i] == cot[i + 2]:
                    if index % 2 == 0:
                        alp[index], alp[index + 1] = alp[index + 1], '_'
                    elif index != len(alp) - 1:
                        alp[index] = '_'
                        alp.insert(index + 1, '_')
                    alp.append(cot[i])
                elif i + 3 >= -len(cot) and cot[i] == cot[i + 3] != cot[i + 2]:
                    if index % 2 == 1:
                        alp[index] = '_'
                        alp.append(cot[i])
                        alp.append(alp[index + 2])
                        alp[index + 2] = '_'
                    else:
                        alp.extend([alp[index + 2], cot[i]])
                        alp[index], alp[index + 1] = alp[index + 1], '_'
            elif cot[i] == cot[i + 1] and index % 2 == 1:
                alp.append(cot[i])
                alp[index] = '_'
    for i in range(len(alp)):
        if len(alp) > 1 and i % 2 == 1:
            if find_one(alp[i], cot) and find_one(alp[i - 1], cot):
                alp[i], alp[i - 1] = alp[i - 1], alp[i]
    alp.reverse()
    list_alp = ''.join(alp)
    print(f"Sure! It is {cus_roman_to_ara(cot, list_alp)} using {list_alp}")
