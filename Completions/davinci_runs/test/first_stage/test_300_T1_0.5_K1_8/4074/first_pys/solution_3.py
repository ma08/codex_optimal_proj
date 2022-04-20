

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    t = int(input())
    for _ in range(t):
        n, k = [int(i) for i in input().split()]
        ans = 0
        for i in range(1, k + 1):
            if n % i == 0:
                ans = n // i
                break
        print(ans)


if __name__ == "__main__":
    main('shovels')