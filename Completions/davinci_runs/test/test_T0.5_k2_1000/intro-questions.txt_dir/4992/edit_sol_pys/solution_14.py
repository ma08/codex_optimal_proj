
import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n = int(input())
    a = input().split()
    a = [int(i) for i in a]
    a.reverse()

    if n == 2:
        if a[0] == a[1]:
            print('2 1')
        else:
            print('impossible')
    else:
        is_possible = True
        for i in range(1, n):
            if a[i] > a[i-1]:
                is_possible = False
        if is_possible:
            print(' '.join([str(i) for i in range(n, 0, -1)]))
        else:
            print('impossible')

if __name__ == "__main__":
    main('sort')
