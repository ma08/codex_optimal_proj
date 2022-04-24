

import sys

def main():
    input = sys.stdin.readline()
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    cnt = [0] * (10 ** 5 + 1)
    for i in range(n - 1):
        t, x, y = a[i]
        if x + y > t:
            print("No")
            sys.exit()
        if (t - (x + y)) % 2 == 1:
            print("No")
            sys.exit()

    print("Yes")

if __name__ == '__main__':
    main()
