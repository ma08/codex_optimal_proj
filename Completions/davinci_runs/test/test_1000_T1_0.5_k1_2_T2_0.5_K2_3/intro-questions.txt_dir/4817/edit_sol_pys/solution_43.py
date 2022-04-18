
from __future__ import print_function

import sys
from collections import defaultdict

def main():
    line = sys.stdin.readline()
    x = int(line.strip())
    digits = list(line.strip())
    digit_counts = defaultdict(int)
    for digit in digits:
        digit_counts[digit] += 1

    # find the first digit that is smaller than the digit to its right
    for i, digit in enumerate(digits[:-1]):
        if digit < digits[i+1]:
            # find the smallest digit that is larger than the digit to its right 
            smallest_digit = digits[i+1]
            smallest_digit_index = i+1
            for j in range(i+2, len(digits)):
                if digits[j] < smallest_digit and digits[j] > digit:
                    smallest_digit = digits[j]
                    smallest_digit_index = j

            # swap the two digits
            digits[i], digits[smallest_digit_index] = digits[smallest_digit_index], digits[i]
            break

    # sort the digits to the right of the swapped digit in ascending order
    digits[i+1:] = sorted(digits[i+1:])

    # if the number is unchanged, then there is no next smallest number
    if x == int(''.join(digits)):
        print(0)
    else:
        print(''.join(digits))

if __name__ == '__main__':
    main()
