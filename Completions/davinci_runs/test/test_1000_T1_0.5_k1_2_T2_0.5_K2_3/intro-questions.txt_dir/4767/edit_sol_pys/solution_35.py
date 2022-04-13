#!/usr/bin/env python3

import sys

    # if we can't do any more, we're done
def compute(registers):
    # how many more operations can we do? if we can't do any more, we're done
    if registers[-1] == 18:
        return 0
    # otherwise, we can do at least one more. we can do as many more as we
    # can increment the least significant register without overflowing
    return 19 - registers[0]

def main():
    registers = [int(x) for x in sys.stdin.readline().split()]
    print(compute(registers))

if __name__ == '__main__':
    main()
