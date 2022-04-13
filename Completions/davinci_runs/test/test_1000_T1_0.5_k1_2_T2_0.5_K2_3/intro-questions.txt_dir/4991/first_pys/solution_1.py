

#!/usr/bin/env python3

def hailstone_sum(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + hailstone_sum(n // 2)
    else:
        return n + hailstone_sum((3 * n) + 1)

def main():
    n = int(input())
    print(hailstone_sum(n))

if __name__ == '__main__':
    main()