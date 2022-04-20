

#!/usr/bin/env python3

def main():
    test_cases = int(input())

    for i in range(test_cases):
        a, b, c = map(int, input().split())
        while a < b:
            b -= 1
        while b < c:
            c -= 1
        while a < c:
            c -= 1
        print(a + b - c)
        print(a, b, c)

if __name__ == '__main__':
    main()