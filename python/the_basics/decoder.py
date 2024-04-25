# Decoder program made for an unnamed publication's qualification test.
# Utilizes coding_qual_input.txt in assets folder
# I'm not going to post the description of this task here so that way someone can't just hop on to github and use my solution.

file_path = 'assets/coding_qual_input.txt'
# I want to have a dictionary of our input so I can quickly decode the solution
pairs_dict = {}

def main():
    # First we need our list
    load_list()
    # I want to work on an array of the keys to begin decoding the message
    decode(sorted(pairs_dict.keys()))

def decode(message_file):
    # We need to build our pyramid
    pyramid = create_pyramid(message_file)
    for step in pyramid:
        print(pairs_dict[step[-1]], end=' ')


def create_pyramid(array):
    pyramid = []
    step = 1
    index = 0
    while index < len(array):
        # I'm going to assume we don't want to be able to Christmas tree this pyramid
        if index + step > len(array):
            break
        pyramid.append(array[index:index + step])
        index += step
        step += 1
    return pyramid

def print_pyramid(pyramid):
    # Naturally this function isn't going to be all that graceful. More of a mountain on the right after 3 digits.
    for i in range(len(pyramid)):
        print(' ' * (len(pyramid) - (i + 1)), end=' ')
        for num in pyramid[i]:
            print(num, end=' ')
        print()

def load_list():
    with open(file_path, 'r') as file:
        for line in file:
            number, word = line.strip().split()
            pairs_dict[int(number)] = word

if __name__ == '__main__':
    main()