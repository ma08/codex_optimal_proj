#!/usr/bin/env python3

import sys

def main():
    # Read input and create list
    input_list = [int(x) for x in sys.stdin.readline().split()]

    # Sort the list
    input_list.sort()

    # Calculate maximum area
    max_area = input_list[0] * input_list[2]

    print(max_area)

if __name__ == "__main__":
    main()
