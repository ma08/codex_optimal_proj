

import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)

    if p == q:
        print('YES')
        sys.exit(0)

    for i in range(n):
        for j in range(i + 1, n):
            p[i], p[j] = p[j], p[i]
            if p == q:
                print('YES')
                sys.exit(0)
            p[i], p[j] = p[j], p[i]

    print('NO')

if __name__ == '__main__':
    main()