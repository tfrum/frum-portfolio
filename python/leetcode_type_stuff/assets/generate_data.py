import csv
import numpy as np

def generate_data(seed, num_integers, output_file):
    np.random.seed(seed)
    data = np.random.randint(0, 1000000, num_integers)

    np.savetxt(output_file, data, delimiter=',', fmt='%d')

def main():
    generate_data(123, 1000000, 'generated_data.csv')

if __name__ == '__main__':
    main()
