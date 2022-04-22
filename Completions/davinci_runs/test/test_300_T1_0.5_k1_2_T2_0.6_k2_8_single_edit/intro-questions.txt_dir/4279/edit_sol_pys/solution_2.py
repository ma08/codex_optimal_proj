

import os
import sys

def get_file_path(n):
    return os.path.join(sys.path[0], n)

def get_input_file_path(n):
    name = 'input-{}.txt'.format(n)
    return get_file_path(name)

def get_output_file_path(n):
    name = 'output-{}.txt'.format(n)
    return get_file_path(name)

def main():
    input_file_path = get_input_file_path(1)
    output_file_path = get_output_file_path(1)
    with open(input_file_path, 'r') as fin:
        with open(output_file_path, 'w') as fout:
            for line in fin:
                n = int(line)
                fout.write(str(find(n)) + '\n')

def find(n):
    if n <= 3:
        return n
    return find(n - 1) + find(n - 2) + find(n - 3)

if __name__ == '__main__':
    main()
