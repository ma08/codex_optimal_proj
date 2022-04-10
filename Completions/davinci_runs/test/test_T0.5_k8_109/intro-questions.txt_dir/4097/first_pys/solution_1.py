

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        sys.exit(0)

    if n == 2:
        if a[0] == a[1]:
            print(0)
        else:
            print(1)
        sys.exit(0)

    d = a[1] - a[0]
    changed = 0
    for i in range(1, n):
        if a[i] != a[i-1] + d:
            changed += 1
            if changed > 1:
                print(-1)
                sys.exit(0)
            if a[i] == a[i-1] + d - 1:
                a[i] += 1
            elif a[i] == a[i-1] + d + 1:
                a[i] -= 1
            else:
                print(-1)
                sys.exit(0)
    print(changed)


if __name__ == '__main__':
    main()