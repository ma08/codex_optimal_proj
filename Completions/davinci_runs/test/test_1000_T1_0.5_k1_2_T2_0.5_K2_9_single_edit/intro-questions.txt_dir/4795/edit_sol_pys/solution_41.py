

import sys

def main():
    n = read_int()
    nums = [read_int() for _ in range(n)]
    result = 0
    for num in nums:
        result += solve(num)
    print(result)


def solve(num):
    digits = str(num)
    if len(digits) == 1:
        return int(digits)
    else:
        return int(digits[0])**(len(digits)-1) + int(digits[1:])


def read_int():
    return int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()
