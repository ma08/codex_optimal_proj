#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline().strip())
    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline().strip()))
    numbers = set(numbers)
    if len(numbers) == max(numbers):
        print("good job")
    else:
        for i in range(1,max(numbers)+1):
            if i not in numbers:
                print(i)

if __name__ == '__main__':
    main()
