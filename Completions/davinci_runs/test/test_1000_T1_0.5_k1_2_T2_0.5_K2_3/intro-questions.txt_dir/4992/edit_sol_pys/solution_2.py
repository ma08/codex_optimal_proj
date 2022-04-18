

import sys

def main(problem_name):
    sys.stdin = open(problem_name + '.in', 'r')
    sys.stdout = open(problem_name + '.out', 'w')

    n = int(input())
    s = raw_input().split()
    s = [int(i) for i in s]
    s.reverse()

    if n == 2:
        if s[0] == s[1]:
            print('2 1')
        else:
            print('impossible')
    else:
        is_possible = True
        for i in range(1, n):
            if s[i] > s[i-1]:
                is_possible = False
        if is_possible:
            print(' '.join([str(i) for i in range(n, 0, -1)]))
        else:
            print('impossible')

if __name__ == "__main__":
    main('exam')
