

import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline().strip()))
    numbers_set = set(numbers[:-1])
    if len(numbers_set) == numbers[-1] - 1:
        print("good job")
    else:
        for i in range(1,numbers[-1]):
            if i not in numbers_set:
                print(i)

if __name__ == '__main__':
    main()
