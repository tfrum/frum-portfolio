ronum_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
ronum = "MMMCMXCIX"

def ronum_value(numeral):
    return ronum_dict[numeral]



def main():
    sum = 0
    prevValue = 0
    for numeral in ronum:
        value = ronum_value(numeral)

        if value > prevValue:
            sum -= prevValue
            sum += value - prevValue
        else:
            sum += value

        prevValue = value
    print(sum)

if __name__ == '__main__':
    main()

