

import sys

def main():
    n = int(input())
    s = input()
    if n % 3 != 0:
        return -1

    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')

    if zeros == ones == twos:
        return s

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
