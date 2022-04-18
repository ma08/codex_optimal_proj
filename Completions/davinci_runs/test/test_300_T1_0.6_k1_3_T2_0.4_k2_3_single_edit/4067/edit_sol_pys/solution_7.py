

import sys

def main():
    n = int(input())
    s = input()
    if n % 3 != 0 or n == 0:
        return '-1'

    zeros = s.count('0')
    ones = s.count('1')
    twos = s.count('2')

    if zeros == ones == twos:
        return s

    if zeros > ones:
        s = s.replace('0', 'x', diff)
        s = s.replace('1', '0', diff)
        s = s.replace('x', '1', diff)
    else:
        s = s.replace('1', 'x', diff)
        s = s.replace('0', '1', diff)
        s = s.replace('x', '0', diff)

    return s

if __name__ == '__main__':
    print(main())
