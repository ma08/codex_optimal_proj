#!/usr/bin/env python

import sys


def read_file(filename):
    pass


def write_file(filename, data):
    pass



def main():
    if len(sys.argv) != 3:
        print("Usage: %s <input file> <output file>" % sys.argv[0])
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read data from file
    data = read_file(input_file)

    # write data to file
    write_file(output_file, data)


if __name__ == "__main__":
    main()
