

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

    if zeros > ones:
        s = s.replace('0', 'x', zeros - ones)
        s = s.replace('1', '0', zeros - ones)
        s = s.replace('x', '1', zeros - ones)
    else:
        s = s.replace('1', 'x', ones - zeros)
        s = s.replace('0', '1', ones - zeros)
        s = s.replace('x', '0', ones - zeros)

    return s

if __name__ == '__main__':
    print(main())
