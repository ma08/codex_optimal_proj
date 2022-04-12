
import sys

def main():
    num_numbers = sys.stdin.readline()
    numbers = []
    for i in range(int(num_numbers)):
        numbers.append(sys.stdin.readline().rstrip())
    if sorted(numbers) == numbers:
        print('INCREASING')
    elif sorted(numbers, reverse=True) == numbers:
        print('DECREASING')
    else:
        print('NEITHER')

if __name__ == '__main__':
    main()
