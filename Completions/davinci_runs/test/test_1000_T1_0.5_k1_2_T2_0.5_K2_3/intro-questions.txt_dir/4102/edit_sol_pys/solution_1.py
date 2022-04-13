#!/usr/bin/env python3

import sys

def is_lucky(number):
    if len(str(number)) % 2 == 0:
        half_len = len(str(number)) // 2
        first_half = number[:half_len]
        second_half = number[half_len:]
        if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
            return True
        else:
            return False
    else:
        return False

def main():
    number = int(input())
    if is_lucky(number):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
