from BFPRT import bfprt

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def main():
    filename = 'assets/numbers.txt'
    k = 5
    numbers = read_numbers_from_file(filename)
    kth_smallest = bfprt(numbers, k)
    print(f"The {k}-th smallest element in the file is {kth_smallest}")


if __name__ == "__main__":
    main()