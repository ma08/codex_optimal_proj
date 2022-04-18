#!/usr/bin/env python3


def factorial(n):
    if n == 0:
        return 1;
    return n * factorial(n-1)

def main():
    num_cases = int(input().strip())
    for i in range(num_cases):
        n = int(input().strip())
        print(factorial(n))

if __name__ == '__main__':
    main()
