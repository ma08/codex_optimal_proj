
import sys

def main():
    num_numbers = int(sys.stdin.readline().rstrip())
    numbers = []
    for i in range(num_numbers):
        numbers.append(int(sys.stdin.readline().rstrip()))
    if sorted(numbers) == numbers:
        print('YES')
    elif sorted(numbers, reverse=True) == numbers:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
