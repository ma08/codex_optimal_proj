#!/usr/bin/env python3

import sys

def main():
    numbers = [int(x) for x in sys.stdin.readline().split(" ")]
    numbers.sort()
    diff = numbers[2] - numbers[1]
    print(numbers[1] + diff)

if __name__ == '__main__':
    main()
