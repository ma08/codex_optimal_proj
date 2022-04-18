

import sys

def main():
    num_numbers = int(sys.stdin.readline())
    numbers = []
    for i in range(num_numbers):
        numbers.append(sys.stdin.readline().rstrip())
    if sorted(numbers) == numbers:
        print('YES')
    elif sorted(numbers, reverse=True) == numbers:
        print('YES')
    else:
        print('NEITHER')

if __name__ == '__main__':
    main()
