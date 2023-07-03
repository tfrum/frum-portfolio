ronum_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
intnum = 1994


def main():
    output = ""
    opnum = intnum
    len_num = len(str(opnum))

    for i in range(len_num):
        position = len_num - i
        temp_int = opnum - (opnum % (10**(len_num - i - 1)))
        if temp_int != 0:
            output += break_down(temp_int, position)
        opnum -= temp_int

    print(output)


def get_numeral(num):
    for key, value in ronum_dict.items():
        if num == value:
            return str(key)


def break_down(num, position):
    return_string = ""
    count = num // (10**(position - 1))

    if num in ronum_dict.values(): # cases 1, 5, and 10, e.g. I, V, X
        return get_numeral(num)

    elif count in (2, 3): # cases 2 and 3, e.g. II, III
        for i in range(count):
            return_string += get_numeral(num // count)

    elif count in (4, 9): # cases 4 and 9 e.g. IX, IV
        for key, value in ronum_dict.items():
            if num < value:
                return get_numeral(value - num) + str(key)

    else: # cases 6, 7, and 8 e.g. VI, VII, VIII
        return_string += get_numeral(5 * (10 ** (position - 1)))
        for i in range(count - 5):
            return_string += get_numeral(num // count)

    return return_string

if __name__ == '__main__':
    main()
