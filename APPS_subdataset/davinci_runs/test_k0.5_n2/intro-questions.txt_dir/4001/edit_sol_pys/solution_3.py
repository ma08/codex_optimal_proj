
import sys

def main():
    n = int(input())
    divisors = [int(x) for x in input().split()]

    x = 1
    y = 1
    for i in range(n):
        if i < n // 2:
            x *= divisors[i]
        else:
            y *= divisors[i]

    print(x, y, end=' ')

if __name__ == '__main__':
    main()
