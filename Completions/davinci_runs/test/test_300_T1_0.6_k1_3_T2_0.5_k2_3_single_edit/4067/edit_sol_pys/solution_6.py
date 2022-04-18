

import sys

def main():
    n = int(input())
    s = input()
    if n % 3 != 0:
        return -1

    zero = s.count('0')
    one = s.count('1')
    two = s.count('2')

    if zero == one == two:
        return s

    diff = abs(zero - one) // 2
    if zero > one:
        s = s.replace('0', 'x', 1)
        s = s.replace('1', '0', 1)
        s = s.replace('x', '1', 1)
    else:
        s = s.replace('1', 'x', 1)
        s = s.replace('0', '1', 1)
        s = s.replace('x', '0', 1)

    return s

if __name__ == '__main__':
    sys.stdout.write(main())
