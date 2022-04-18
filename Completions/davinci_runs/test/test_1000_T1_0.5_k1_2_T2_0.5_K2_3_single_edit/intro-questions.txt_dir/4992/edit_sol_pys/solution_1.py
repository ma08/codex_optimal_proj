

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    s = input().split()
    s = [int(i) - 1 for i in s]
    s.reverse()

    is_possible = True
    for i in range(n):
        if s[i] != i:
            is_possible = False
    if is_possible:
        print(' '.join([str(i) for i in range(n, 0, -1)]))
    else:
        print('impossible')

if __name__ == "__main__":
    main('exam')
