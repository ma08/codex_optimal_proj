

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

    diff = abs(zeros - twos) // 2
    if zeros > twos:
        s = s.replace('0', 'z', 1)
        s = s.replace('2', '0', 1)
        s = s.replace('z', '2', 1)
    elif twos > zeros:
        s = s.replace('2', 'z', 1)
        s = s.replace('0', '2', 1)
        s = s.replace('z', '0', 1)

    return s

if __name__ == '__main__':
    print(main())
