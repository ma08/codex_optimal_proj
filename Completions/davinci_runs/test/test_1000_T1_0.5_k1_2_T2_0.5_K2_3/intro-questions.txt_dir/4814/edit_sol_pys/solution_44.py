import sys
import math

def main():
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        num_numbers = sys.stdin.readline().rstrip()
        numbers = []
        for j in range(int(num_numbers)):
            numbers.append(int(sys.stdin.readline().rstrip()))
        if sorted(numbers) == numbers:
            print('YES')
        elif sorted(numbers, reverse=True) == numbers:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
