
import sys

def main():
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    numbers.sort()
    diff = numbers[1] - numbers[0]
    if numbers[2] - numbers[1] == diff:
        print(numbers[2] + diff)
    elif numbers[1] - numbers[0] == diff:
        print(numbers[0] - diff)
    else:
        print(numbers[1] + diff)

if __name__ == "__main__":
    main()
