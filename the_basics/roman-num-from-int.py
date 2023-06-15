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




def get_numeral(num):
    for key, value in ronum_dict.items():
        if num == value:
            return str(key)


def break_down(num):
    if num in ronum_dict.values():
        return get_numeral(num)
    else:
        for key, value in ronum_dict.items():
            if num < value:
                return get_numeral(value - num) + str(key)
        


def main():
    output = ""
    opnum = intnum
    len_num = len(str(opnum))

    for i in range(len_num):
        # this gets us whole numbers in each place of the number

        temp_int = opnum - (opnum % (10**(len_num - i - 1)))
        output += break_down(temp_int)
        opnum -= temp_int

    print(output)
    # remember to add the remainder of opnum 


if __name__ == '__main__':
    main()
