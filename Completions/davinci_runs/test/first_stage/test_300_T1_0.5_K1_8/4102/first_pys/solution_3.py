

import sys

def main():
    for line in sys.stdin:
        print('Yes' if is_happy(line.strip()) else 'No')

def is_happy(number):
    seen_numbers = set()
    while True:
        sum_of_squares = sum(map(lambda digit: int(digit)**2, number))
        if sum_of_squares == 1:
            return True
        elif sum_of_squares in seen_numbers:
            return False
        else:
            seen_numbers.add(sum_of_squares)
            number = str(sum_of_squares)

main()