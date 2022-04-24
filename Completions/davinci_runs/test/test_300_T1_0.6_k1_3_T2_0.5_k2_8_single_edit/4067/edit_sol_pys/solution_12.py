

import sys

def main():
    n = int(input())
    s = input().strip()
    if n % 3 != 0:
        print(-1)
        sys.exit(0)

    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')

    if zeros == ones == twos:
        print(s)
        sys.exit(0)

    diff = abs(zeros - ones) // 2
    if zeros > ones:
        s = s.replace('0', 'x', 1)
        s = s.replace('1', '0', 1)
        s = s.replace('x', '1', 1)
    else:
        s = s.replace('1', 'x', 1)
        s = s.replace('0', '1', 1)
        s = s.replace('x', '0', 1)

    print(s)

if __name__ == '__main__':
    main()
