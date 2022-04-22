

import sys

def main():
    N = int(input())
    s = input()
    assert(N % 3 == 0 and len(s) == N)

    count_0 = s.count('0')
    count_1 = s.count('1')
    count_2 = s.count('2')

    if count_0 == count_1 == count_2:
        print(s)
        sys.exit(0)

    n = N // 3
    if count_0 == n and count_1 == n:
        print(s.replace('2', '0', 1), end='')
        sys.exit(0)
    if count_0 == n and count_2 == n:
        print(s.replace('1', '0', 1), end='')
        sys.exit(0)
    if count_1 == n and count_2 == n:
        print(s.replace('0', '1', 1), end='')
        sys.exit(0)

    if count_0 == n:
        print(s.replace('1', '0', 1), end='')
        sys.exit(0)
    if count_1 == n:
        print(s.replace('2', '1', 1), end='')
        sys.exit(0)
    if count_2 == n:
        print(s.replace('0', '2', 1), end='')
        sys.exit(0)

    if count_0 > count_1:
        print(s.replace('0', '2', 1), end='')
        sys.exit(0)
    if count_0 > count_2:
        print(s.replace('0', '1', 1), end='')
        sys.exit(0)
    if count_1 > count_0:
        print(s.replace('1', '0', 1), end='')
        sys.exit(0)
    if count_1 > count_2:
        print(s.replace('1', '2', 1), end='')
        sys.exit(0)
    if count_2 > count_0:
        print(s.replace('2', '0', 1))
        sys.exit(0)
    if count_2 > count_1:
        print(s.replace('2', '1', 1))
        sys.exit(0)

main()
