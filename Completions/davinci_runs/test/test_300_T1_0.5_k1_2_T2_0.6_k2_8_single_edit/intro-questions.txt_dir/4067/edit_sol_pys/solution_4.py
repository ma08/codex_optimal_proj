

import sys

def main():
    N = int(input())
    S = input()
    assert(N % 3 == 0)

    count_0 = S.count('0')
    count_1 = S.count('1')
    count_2 = S.count('2')

    if count_0 == count_1 == count_2:
        print(S)
        sys.exit(0)

    n = N // 3
    if count_0 == n and count_1 == n:
        print(S.replace('2', '0', 1))
        sys.exit(0)
    if count_0 == n and count_2 == n:
        print(S.replace('1', '0', 1))
        sys.exit(0)
    if count_1 == n and count_2 == n:
        print(S.replace('0', '1', 1))
        sys.exit(0)

    if count_0 == n:
        print(S.replace('1', '0', 1))
        sys.exit(0)
    if count_1 == n:
        print(S.replace('2', '1', 1))
        sys.exit(0)
    if count_2 == n:
        print(S.replace('0', '2', 1))
        sys.exit(0)

    if count_0 > count_1:
        print(S.replace('0', '2', 1))
        sys.exit(0)
    if count_0 > count_2:
        print(S.replace('0', '1', 1))
        sys.exit(0)
    if count_1 > count_0:
        print(S.replace('1', '0', 1))
        sys.exit(0)
    if count_1 > count_2:
        print(S.replace('1', '2', 1))
        sys.exit(0)
    if count_2 > count_0:
        print(S.replace('2', '0', 1))
        sys.exit(0)
    if count_2 > count_1:
        print(S.replace('2', '1', 1))
        sys.exit(0)

main()
