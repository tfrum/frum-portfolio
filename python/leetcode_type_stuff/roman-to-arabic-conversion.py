NUMERALS = [ "M", "D", "C", "L", "X", "V", "I" ]

NUMERAL_VALS = { "M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1 }

def roman_to_arabic(roman_str):
    arabic_val = 0
    last_val = 1000

    for i in range(len(roman_str)):
        roman_int = roman_str[i]
        roman_val = NUMERAL_VALS[roman_int]

        if roman_val > last_val:
            arabic_val -= last_val
            arabic_val += roman_val - last_val
        else:
            arabic_val += roman_val

        last_val = roman_val

    return arabic_val

def arabic_to_roman(arabic_str):
    remainder = int(arabic_str)
    roman_str = ""
    roman_index = 0
    coeff = 1
    base = 1000
    arabic_val = 0
    count = 0

    while remainder > 0:
        arabic_val = base * coeff
        count = int(remainder // arabic_val)

        print(f"count: {count} remainder: {remainder} arabic: {arabic_val}")

        if count > 0:
            roman_str += NUMERALS[roman_index] * count
            remainder -= count * arabic_val

        if coeff == 1:
            print(f"{(arabic_val / 10) * 9}")
            if remainder >= (arabic_val / 10) * 9:
                remainder -= (arabic_val / 10) * 9
                roman_str += NUMERALS[roman_index+2] + NUMERALS[roman_index]
            elif remainder >= (arabic_val / 2):
                print(f"{arabic_val / 2}")
                remainder -= (arabic_val / 2) + 1
                roman_str += NUMERALS[roman_index+1] + NUMERALS[roman_index+2]

            coeff = 5
            base /= 10
        else:
            coeff = 1

        print(f"{roman_str}")
        
        roman_index += 1

    return roman_str


def main():
    roman_str = arabic_to_roman(input(""))
    arabic_val = roman_to_arabic("MCMXCVI")

    print(f"A->R: {roman_str} R->A: {arabic_val}")


if __name__ == "__main__":
    main()