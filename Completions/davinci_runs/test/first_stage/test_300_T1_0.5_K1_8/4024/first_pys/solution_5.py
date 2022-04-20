

import sys

def main():
    n, k = map(int, input().split())
    s = input()

    if k > n:
        print(-1)
        return

    if k == n:
        print(0)
        return

    if k == 1:
        print(n)
        return

    if k == 2:
        if len(set(s)) == 1:
            print(n)
            return
        else:
            print(n - 1)
            return

    print(n - k)

if __name__ == "__main__":
    main()