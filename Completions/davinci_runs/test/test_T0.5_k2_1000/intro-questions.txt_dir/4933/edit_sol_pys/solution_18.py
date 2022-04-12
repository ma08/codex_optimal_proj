
import sys

def main():
    numbers = [int(x) for x in sys.stdin.readline().split()] # list comprehension
    numbers.sort()
    diff = numbers[1] - numbers[0]
    print(numbers[2] + diff)

if __name__ == '__main__':
    main()
